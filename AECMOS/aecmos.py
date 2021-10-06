import argparse
import glob
import os
import librosa
import requests

import numpy as np
import pandas as pd

from tqdm import tqdm

SCORING_URL = '<Insert the URL we provide here>'
AUTH = ('<Insert the username we provide here>',
        '<Insert the password we provide here>')


SCENARIOS = [
    'doubletalk_with_movement',
    'doubletalk',
    'farend_singletalk_with_movement',
    'farend_singletalk',
    'nearend_singletalk'
]
SAMPLE_RATE = 16000


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True,
                        help='Path to directory containing enhanced nearend speech')
    parser.add_argument('-d', '--dataset', required=True,
                        help='Path to directory containing loopback and mic files, needs to be same relative level as "input"')
    parser.add_argument(
        '--score_file', help='Path to file for saving scores, optional')

    return parser.parse_args()


def main(input_dir, dataset_dir, score_file):
    clips = glob.glob(os.path.join(input_dir, '**', '*.wav'), recursive=True)

    scores = []
    for clip_path in tqdm(clips):
        lpb_path, mic_path = get_lpb_mic_paths(
            input_dir, dataset_dir, clip_path)

        lpb_sig, mic_sig, enh_sig = read_and_process_audio_files(
            lpb_path, mic_path, clip_path)

        clip_scores = get_score(lpb_sig, mic_sig, enh_sig,
                                get_clip_scenario(os.path.basename(clip_path)))

        score = {'file': os.path.basename(clip_path)}
        score.update(clip_scores)

        scores.append(score)

    scores_df = pd.DataFrame(scores)
    print(
        f'Mean echo MOS is {scores_df.echo_mos.mean()}, other degradation MOS is {scores_df.deg_mos.mean()}')

    if score_file:
        scores_df.to_csv(score_file, index=False)


def get_lpb_mic_paths(input_dir, dataset_dir, clip_path):
    relative_path = os.path.relpath(clip_path, input_dir)

    clip_filename = os.path.basename(clip_path)
    clip_hash = get_clip_hash(clip_filename)
    clip_scenario = get_clip_scenario(clip_filename)

    relative_dir = os.path.split(relative_path)[0]

    lpb_filename = f'{clip_hash}_{clip_scenario}_lpb.wav'
    lpb_path = os.path.join(dataset_dir, relative_dir, lpb_filename)

    mic_filename = f'{clip_hash}_{clip_scenario}_mic.wav'
    mic_path = os.path.join(dataset_dir, relative_dir, mic_filename)

    return lpb_path, mic_path


def get_clip_hash(clip_file_name):
    # In case a path is passed
    input_parts = os.path.split(clip_file_name)
    return input_parts[-1][:22]


def get_clip_scenario(clip_file_name):
    scenario = next(
        (s for s in SCENARIOS if s in clip_file_name), None)
    assert scenario is not None

    return scenario


def read_and_process_audio_files(lpb_path, mic_path, clip_path):
    lpb_sig, _ = librosa.load(lpb_path, sr=SAMPLE_RATE)
    mic_sig, _ = librosa.load(mic_path, sr=SAMPLE_RATE)
    enh_sig, _ = librosa.load(clip_path, sr=SAMPLE_RATE)

    # Make the clips the same length
    min_len = np.min([len(lpb_sig), len(mic_sig), len(enh_sig)])
    lpb_sig = lpb_sig[:min_len]
    mic_sig = mic_sig[:min_len]
    enh_sig = enh_sig[:min_len]

    if is_interspeech2021_clip(clip_path):
        lpb_sig, mic_sig, enh_sig = process_interspeech2021(
            lpb_sig, mic_sig, enh_sig, clip_path)

    return lpb_sig, mic_sig, enh_sig


def is_interspeech2021_clip(clip_path):
    # This function can be used with your own custom heuristic
    # Here we assume the dataset name is somewhere on the full clip path
    return 'test_set_interspeech2021' in clip_path


def process_interspeech2021(lpb_sig, mic_sig, enh_sig, clip_path):
    clip_name = os.path.basename(clip_path)
    clip_scenario = get_clip_scenario(clip_name)
    if clip_scenario in ['doubletalk_with_movement', 'doubletalk']:
        silence_duration = 15 * SAMPLE_RATE  # in seconds
        rating_dt_length = int((len(enh_sig) - silence_duration) / 2)

        if rating_dt_length > 0:
            lpb_sig = lpb_sig[-rating_dt_length:]
            mic_sig = mic_sig[-rating_dt_length:]
            enh_sig = enh_sig[-rating_dt_length:]

    elif clip_scenario in ['farend_singletalk_with_movement', 'farend_singletalk']:
        rating_fest_length = int(len(enh_sig) / 2)

        lpb_sig = lpb_sig[-rating_fest_length:]
        mic_sig = mic_sig[-rating_fest_length:]
        enh_sig = enh_sig[-rating_fest_length:]

    elif clip_scenario == 'nearend_singletalk':
        pass
    else:
        raise Exception()

    return lpb_sig, mic_sig, enh_sig


def get_score(lpb_sig, mic_sig, enh_sig, scenario):
    audio_data = {
        'lpb': lpb_sig.tolist(),
        'mic': mic_sig.tolist(),
        'enh': enh_sig.tolist(),
        'scenario': scenario
    }

    response = requests.post(SCORING_URL, json=audio_data, auth=AUTH)
    json_body = response.json()

    if 'error' in json_body:
        raise Exception(json_body['error'])

    return json_body


if __name__ == '__main__':
    args = parse_args()

    input_dir = args.input
    dataset_dir = args.dataset
    score_file = args.score_file

    main(input_dir, dataset_dir, score_file)
