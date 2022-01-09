# AECMOS

We've created a web API for you to evaluate clips with regards to echo ratings and other degradations ratings.

To get access, email aec_challenge@microsoft.com with the following details:
 - Contact Name
 - Research Group/Institute/Company
 - Purpose of using AECMOS

We will send you the *SCORING_URL* and *AUTH* keys that can be used with the script or with your own code.

## NB! 
When using AECMOS with the interspeech 2021 test set, make sure to only send the actual parts to be rated, as the clips have been made longer to allow models to converge.

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
