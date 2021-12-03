# Baseline AEC model

The directory includes inference scripts for the baseline model used in the challenge.

## Usage

In order to try the baseline model on your files, run

```sh
python enhance.py --data_dir INPUT_DIRECTORY --output_dir OUTPUT_DIRECTORY
```

The input directory should include microphone and far end signals in the format used in the challenge test sets. 
Specifically, the script assumes the microphone and far end files end with `_mic.wav` and `_lpb.wav`, respectively.
The required packages are listed in the `requirements.txt` file.