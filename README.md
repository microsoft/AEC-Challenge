# AEC Challenge
The ICASSP 2022 Acoustic Echo Cancellation Challenge is intended to stimulate research in the area of acoustic echo cancellation (AEC), which is an important part of speech enhancement and still a top issue in audio communication and conferencing systems. This is the third AEC challenge and it is enhanced by including mobile scenarios, adding speech recognition rate in the challenge goal metrics, and making the default sample rate 48 kHz. In this challenge, we open source two large datasets to train AEC models under both single talk and double talk scenarios. These datasets consist of recordings from more than 7,500 real audio devices and human speakers in real environments, as well as a synthetic dataset. We also open source an online subjective test framework and provide an online objective metric service for researchers to quickly test their results. The winners of this challenge are selected based on the average Mean Opinion Score achieved across all different single talk and double talk scenarios, and the speech recognition rate.

For more details about the challenge, please visit the challenge [website](https://www.microsoft.com/en-us/research/academic-program/acoustic-echo-cancellation-challenge-icassp-2022/) and refer to the [paper](https://www.researchgate.net/publication/356204168_ICASSP_2022_Acoustic_Echo_Cancellation_Challenge).



# Repo details
* The datasets directory contains the real and synthetic training datasets and real test sets.
* Test set for the ICASSP 2022 challenge is located at https://github.com/microsoft/AEC-Challenge/tree/main/datasets/test_set_icassp2022.
* Links to newest fullband real-world recordings are located at https://github.com/microsoft/AEC-Challenge/tree/main/datasets/fullband and https://github.com/microsoft/AEC-Challenge/tree/main/datasets/fullband_mobile.

# Usage
1. Set up Git Large File Storage (LFS) for faster download of the datasets. First, [download](https://git-lfs.github.com/) and install the Git LFS client. Then, set up Git LFS for your user account by running:
```
git lfs install
```
2. Clone the repository. 
```
git clone https://github.com/microsoft/AEC-Challenge AEC-Challenge
```



## Citation:
If you use this dataset in a publication please cite the following paper:<br />  

```BibTex
@inproceedings{cutler2022AEC,
  title={ICASSP 2022 Acoustic Echo Cancellation Challenge},
  author={Cutler, Ross and Saabas, Ando and Parnamaa, Tanel and Purin, Marju and Gamper, Hannes and Braun, Sebastian and  Sorensen, Karsten and Aichner, Robert},
  booktitle={ICASSP 2022}
  year={2022},
}
```

If you use the test framework in a publication please cite the following paper:<br />
```BibTex
@inproceedings{cutler2021crowdsourcing,
  title={Crowdsourcing approach for subjective evaluation of echo impairment},
  author={Cutler, Ross and Nadari, Babak and Loide, Markus and Sootla, Sten and Saabas, Ando},
  booktitle={ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={406--410},
  year={2021},
  organization={IEEE}
}
```

## Dataset licenses
MICROSOFT PROVIDES THE DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INLCUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS.

The datasets are provided under the original terms that Microsoft received such datasets. See below for more information about each dataset.

The datasets used in this project are licensed as follows:
1. Clean speech: 
* https://librivox.org/; License: https://librivox.org/pages/public-domain/
* Edinburgh 56 speaker dataset: https://datashare.is.ed.ac.uk/handle/10283/2791; License: https://datashare.is.ed.ac.uk/bitstream/handle/10283/2791/license_text?sequence=11&isAllowed=y 
2. Noise:
* Audioset: https://research.google.com/audioset/index.html; License: https://creativecommons.org/licenses/by/4.0/
* Freesound: https://freesound.org/ Only files with CC0 licenses were selected; License: https://creativecommons.org/publicdomain/zero/1.0/
* Demand: https://zenodo.org/record/1227121#.XRKKxYhKiUk; License: https://creativecommons.org/licenses/by-sa/3.0/deed.en_CA

## Code license
MIT License

Copyright (c) Microsoft Corporation.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
