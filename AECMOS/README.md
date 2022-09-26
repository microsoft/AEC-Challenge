# AECMOS

We have created AECMOS for evaluating audio clips with regards to two categories: echo ratings and other degradations ratings.

We are releasing onnx versions of the AECMOS model. The onnx models and inference script are located in the AECMOS_local directory. 

We no longer update the web API. If you have previously used the web API, please note that the scoring_url is now versioned, e.g. https://dnsmos.azurewebsites.net/v2/aecmos/score-dec indicates version number 2. This way it is easy for you to know which model version you have been using.

Please email aec_challenge@microsoft.com with any questions.

## NB! 
When using AECMOS with the interspeech 2021 or the ICASSP2022 test set, make sure to only send the actual parts to be rated, as the clips have been made longer to allow models to converge.

In the case of _farend-singletalk_ only send the last half of the clip, in the case of _doubletalk_ the last `(length_in_seconds - 15) / 2` seconds should be sent. With _nearend-singletalk_, the whole clip should be sent. An example of this is provided in the provided AECMOS script.

# Citation
If you use AECMOS for a publication please cite the following paper:

```BibTex
@article{purin2021aecmos,
  title={AECMOS: A speech quality assessment metric for echo impairment},
  author={Purin, Marju and Sootla, Sten and Sponza, Mateja and Saabas, Ando and Cutler, Ross},
  journal={arXiv preprint arXiv:2110.03010},
  year={2021}
}
```
