import math
import os

import librosa
import numpy as np
import soundfile as sf

def magphasor(complexspec):
    """Decompose a complex spectrogram into magnitude and unit phasor.
    m, p = magphasor(c) such that c == m * p.
    """
    mspec = np.abs(complexspec)
    pspec = np.empty_like(complexspec)
    zero_mag = mspec == 0.  # fix zero-magnitude
    pspec[zero_mag] = 1.
    pspec[~zero_mag] = complexspec[~zero_mag] / mspec[~zero_mag]
    return mspec, pspec


def logpow(sig, floor=-30.):
    """Compute log power of complex spectrum.
    Floor any -`np.inf` value to (nonzero minimum + `floor`) dB.
    If all values are 0s, floor all values to -80 dB.
    """
    log10e = np.log10(np.e)
    pspec = sig.real**2 + sig.imag**2
    zeros = pspec == 0
    logp = np.empty_like(pspec)
    if np.any(~zeros):
        logp[~zeros] = np.log(pspec[~zeros])
        logp[zeros] = np.log(pspec[~zeros].min()) + floor / 10 / log10e
    else:
        logp.fill(-80 / 10 / log10e)

    return logp


def hamming(wsize, hop=None):
    "Compute the Hamming window"

    if hop is None:
        return np.hamming(wsize)

    # for perfect OLA reconstruction in time
    if wsize % 2:  # fix endpoint problem for odd-size window
        wind = np.hamming(wsize)
        wind[0] /= 2.
        wind[-1] /= 2.
    else:  # even-size window
        wind = np.hamming(wsize + 1)
        wind = wind[:-1]

    assert tnorm(wind, hop), \
        "[wsize:{}, hop:{}] violates COLA in time.".format(wsize, hop)

    return wind


def tnorm(wind, hop):
    amp = tcola(wind, hop)
    if amp is None:
        return False
    wind /= amp
    return True


def tcola(wind, _hop):
    wsize = len(wind)
    hsize = 160
    buff = wind.copy()  # holds OLA buffer and account for time=0
    for wi in range(hsize, wsize, hsize):  # window moving forward
        wj = wi + wsize
        buff[wi:] += wind[:wsize - wi]
    for wj in range(wsize - hsize, 0, -hsize):  # window moving backward
        wi = wj - wsize
        buff[:wj] += wind[wsize - wj:]

    if np.allclose(buff, buff[0]):
        return buff[0]

    return None