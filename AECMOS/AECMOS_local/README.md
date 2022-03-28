# AECMOS inference script

* We release the AECMOS onnx model that we have developed as described in the paper (https://arxiv.org/abs/2110.03010). This directory contains the inference script and onnx model for running AECMOS locally.

## Prerequisites
- Python 3.0 and above
- torch 1.9.1.
- numpy 1.21.5
- librosa 0.9.1
- onnxruntime 1.10.0

## Usage:
From the AECMOS onnx directory, run aecmos.py with the following required arguments:
- -talk_type "Specify the scenario: 'st' (far-end single talk), 'nst' (near-end single talk), or 'dt' (double talk)."
- -model_path "Specify the path to the onnx model provided"
- -lpb_path "Specify the path to the lpb audio file"
- -mic_path "Specify the path to the mic audio file"
- -enh_path "Specify the path to the mic audio file"

Use default values for the rest. Run to score the clips.

## NB! 
When using AECMOS with the interspeech 2021 or the ICASSP2022 test set, make sure to only evaluate the actual parts to be rated, as the clips have been made longer to allow models to converge.

In the case of _farend-singletalk_ only send the last half of the clip, in the case of _doubletalk_ the last `(length_in_seconds - 15) / 2` seconds should be sent. With _nearend-singletalk_, the whole clip should be sent. 


## Citation:
The :<br />  
```BibTex
@misc{purin2021aecmos,
    title={AECMOS: A speech quality assessment metric for echo impairment.},
    author={Marju Purin, Sten Sootla, Mateja Sponza, Ando Saabas, and Ross Cutler},
    year={2021},
    eprint={2110.03010v3},
    archivePrefix={arXiv},
    primaryClass={eess.AS}
}
```
