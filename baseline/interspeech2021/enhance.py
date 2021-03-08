import argparse
import glob
import os

import librosa
import numpy as np
import onnxruntime
import soundfile as sf
from tqdm import tqdm

import audio_utils


class DECModel:

    def __init__(self, model_path, window_length, hop_fraction,
                 dft_size, hidden_size, sampling_rate=16000, spectral_floor=-120.0):
        self.hop_fraction = hop_fraction
        self.dft_size = dft_size
        self.hidden_size = hidden_size
        self.sampling_rate = sampling_rate
        self.spectral_floor = spectral_floor
        self.frame_size = int(window_length * sampling_rate)
        self.hop_size = int(window_length * sampling_rate * hop_fraction)
        self.window = audio_utils.hamming(self.frame_size, hop=hop_fraction)
        self.model = onnxruntime.InferenceSession(model_path)

    def calc_features(self, xmag_mic, xmag_far):
        feat_mic = audio_utils.logpow(xmag_mic, floor=self.spectral_floor)
        feat_far = audio_utils.logpow(xmag_far, floor=self.spectral_floor)
        feat = np.concatenate([feat_mic, feat_far])
        feat /= 20.
        feat = feat[np.newaxis, np.newaxis, :]
        feat = feat.astype(np.float32)

        return feat

    def enhance(self, path_mic, path_far, path_out):
        # load inputs
        x_mic, _ = librosa.load(path_mic, sr=self.sampling_rate)
        x_far, _ = librosa.load(path_far, sr=self.sampling_rate)

        # cut to equal length
        min_len = min(len(x_mic), len(x_far))
        x_mic = x_mic[:min_len]
        x_far = x_far[:min_len]

        # zero pad from left
        pad_left, pad_right = self.hop_size, 0
        x_mic = np.pad(x_mic, (pad_left, pad_right))
        x_far = np.pad(x_far, (pad_left, pad_right))

        # init buffers
        num_frames = (len(x_mic) - self.frame_size) // self.hop_size + 1
        x_back = np.zeros(self.frame_size + (num_frames - 1) * self.hop_size)
        h01 = np.zeros((1, 1, self.hidden_size), dtype=np.float32)
        h02 = np.zeros((1, 1, self.hidden_size), dtype=np.float32)

        # frame-wise inference
        for ix_start in range(0, len(x_mic) - self.frame_size, self.hop_size):
            ix_end = ix_start + self.frame_size
            
            cspec_mic = np.fft.rfft(x_mic[ix_start:ix_end] * self.window, self.dft_size)
            xmag_mic, xphs_mic = audio_utils.magphasor(cspec_mic)
            cspec_far = np.fft.rfft(x_far[ix_start:ix_end] * self.window)
            xmag_far = np.abs(cspec_far)
            feat = self.calc_features(xmag_mic, xmag_far)

            inputs = {
                "input": feat, 
                "h01": h01, 
                "h02": h02,
            }
            
            mask, h01, h02 = self.model.run(None, inputs)
            mask = mask[0, 0]
            x_enh = np.fft.irfft(mask * xmag_mic * xphs_mic, self.dft_size)
            x_back[ix_start:ix_end] += x_enh

        return x_back[pad_left:]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Baseline model inference")
    parser.add_argument("--model_path", "-m", help="ONNX model to use for inference.", default="dec-baseline-model-interspeech2021.onnx")
    parser.add_argument("--data_dir", "-d", required=True, help="Directory containing mic and farend files.")
    parser.add_argument("--output_dir", "-o", required=True, help="Output directory to save enhanced output files.")
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        print(f"Creating output directory: {args.output_dir}")
        os.makedirs(args.output_dir)

    sampling_rate = 16000
    model = DECModel(
        model_path=args.model_path,
        window_length=0.02,
        hop_fraction=0.5,
        dft_size=320,
        hidden_size=322,
        sampling_rate=sampling_rate,
        spectral_floor=-120.)

    mic_paths = glob.glob(os.path.join(args.data_dir, "*_mic.wav"))
    for mic_path in tqdm(mic_paths):
        basename = os.path.basename(mic_path)
        farend_path = mic_path.replace("_mic.wav", "_lpb.wav")
        if not os.path.exists(farend_path):
            print("Farend file not found, skipping:", farend_path)
            continue

        out_path = os.path.join(args.output_dir, basename)
        if os.path.exists(out_path):
            print("Enhanced file exists, overwriting:", out_path)
        x_enhanced = model.enhance(mic_path, farend_path, out_path)
        sf.write(out_path, x_enhanced, sampling_rate)