import os, sys 

import numpy as np 
import scipy 
import matplotlib.pyplot as plt

import librosa 

from STFT import create_sftf
from SampleCompse import decompose_stft


def main():

    
    data = scipy.io.loadmat(r"DataSet\G1D1D2\G1D1.mat")

    sa = data["Sa"]    
    
    stft, spectrograms = create_sftf(sa[0,0])
    decompose_stft(spectrograms[0])

    x = 0
    pass 


if __name__ == "__main__":
    main()
