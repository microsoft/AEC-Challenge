
The real dataset files use the following naming conventions:

* Far end single talk, no echo path change
  * GUID_farend_singletalk_lpb.wav
  * GUID_farend_singletalk_mic.wav
* Far end single talk, echo path change
  * GUID_farend_singletalk_with_movement_lpb.wav
  * GUID_farend_singletalk_with_movement_mic.wav
* Near end single talk, no echo path change
  * GUID_nearend_singletalk_mic.wav
* Double talk, no echo path change
  * GUID_doubletalk_lpb.wav
  * GUID_doubletalk_mic.wav
* Double talk, echo path change
  * GUID_doubletalk_with_movement_lpb.wav
  * GUID_doubletalk_with_movement_mic.wav
* Sweep signal for RT60 estimation
  * GUID_sweep_lpb.wav
  * GUID_sweep_mic.wav

The real files were captured on Windows PCs as shown below. Some PCs may have audio DSP processing in the send and/or receive path, even though we used a raw mode to play and capture audio.

![alt text](https://github.com/microsoft/AEC-Challenge/blob/main/images/Recording.png)
