### Overview
The synthetic dataset provides 10,000 examples representing single talk, double talk, near end noise, far end noise, and various nonlinear distortion situations. 
Each example includes a far end speech, echo signal, near end speech and near end microphone signal clip. 
The clips can be linked by the `fileid_{int}` attribute.
The meta.csv file includes information about the synthesis parameters such as source clip ids, speaker ids and signal-to-echo ratios.

For a more detailed description of the generation process, please refer to the [paper](https://arxiv.org/abs/2009.04972).

### Directory contents
`farend_speech` - far end signals, some of these include background noise (indicated by `is_farend_noisy=1` in the meta.csv file).

`echo_signal` - transformed version of far end speech, used as echo signals.

`nearend_speech` - clean near end signals that can be used as targets. Note that these signals are clean and do not include near end noise. The use of near end noise is indicated by `is_nearend_noisy=1` in the meta.csv file. The meta.csv file includes a `nearend_scale` column - if you multiply the scale factor with the near end signal, you get the signal in the same scale as in the `nearend_mic_signal` clip.

`nearend_mic_signal` - near end microphone signals - mixtures of nearend speech and echo signals. The signal-to-echo ratio is indicated in the `ser` column in the meta.csv file. The clips might also include near end noise (indicated by `is_nearend_noisy=1`).
