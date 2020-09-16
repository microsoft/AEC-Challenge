# AEC Challenge
The ICASSP 2021 Acoustic Echo Cancellation Challenge is intended to stimulate research in the area of acoustic echo cancellation (AEC), which is an important part of speech enhancement and still a top issue in audio communication and conferencing systems. Many recent AEC studies report reasonable performance on synthetic datasets where the train and test samples come from the same underlying distribution. However, the AEC performance often degrades significantly on real recordings. Also, most of the conventional objective metrics such as  echo return loss enhancement (ERLE) and perceptual evaluation of speech quality (PESQ) do not correlate well with subjective speech quality tests in the presence of background noise and reverberation found in realistic environments. In this challenge, we open source two large datasets to train AEC models under both single talk and double talk scenarios. These datasets consist of recordings from more than 2,500 real audio devices and human speakers in real environments, as well as a synthetic dataset. We open source an online subjective test framework based on [ITU-T P.808](https://github.com/microsoft/P.808) for researchers to quickly test their results. The winners of this challenge will be selected based on the average P.808 Mean Opinion Score (MOS) achieved across all different single talk and double talk scenarios.

For more details about the challenge, please visit the challenge [website](http://aec-challenge.azurewebsites.net/) and refer to the [paper](https://arxiv.org/abs/2009.04972).

# Repo details
* The datasets directory contains the real and synthetic training datasets and real test sets.

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
For the datasets and the AEC challenge:<br />  

```BibTex
@article{Sridar2020,
  title={ICASSP 2021 Acoustic Echo Cancellation Challenge: Datasets and Testing Framework},
  author={Kusha Sridhar, Ross Cutler, Ando Saabas, Tanel Parnamaa, Hannes Gamper, Sebastian Braun, Robert Aichner, Sriram Srinivasan},
  journal={arXiv preprint arXiv:2009.04972},
  year={2020},
  url={https://arxiv.org/pdf/2009.04972.pdf}
}
```

For the test framework:<br />
```BibTex
@article{naderi2020open,
  title={An Open source Implementation of ITU-T Recommendation P. 808 with Validation},
  author={Naderi, Babak and Cutler, Ross},
  journal={arXiv preprint arXiv:2005.08138},
  year={2020}
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
