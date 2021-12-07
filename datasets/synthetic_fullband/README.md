### Overview

The synthetic dataset provides 10,000 examples at a 48,000 sampling rate representing single talk, double talk, near end noise, far end noise, and various nonlinear distortion situations.
Each example includes a far end speech, echo signal, near end speech, and near end microphone signal clip.
Each clip is 10 seconds long.

### Files

Explanation of the suffixes of the files:
* `_farend.wav` - far end signal, some of the files include background noise (indicated by `is_farend_noisy=1` in the `meta.csv` file);
* `_echo.wav` - echo signal;
* `_nearend.wav` - near end signal, some of the files include background noise (indicated by `is_nearend_noisy=1` in the `meta.csv` file);
* `_mic.wav` - near end microphone signal, i.e. mixtures of near end and echo signals;
* `_target.wav` - near end speech without background noise.

### Download
The data is available for download from the following link:

| Link | MD5 checksum |
| --- | --- |
|[fullband_synthetic.zip (26.4 GB)](https://aecchallengepublic.blob.core.windows.net/icassp2022/fullband_synthetic.zip)|`4016e887707f5570069960ebf263b644` |