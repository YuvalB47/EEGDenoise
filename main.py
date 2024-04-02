import os, sys 

import numpy as np 
import scipy 
import matplotlib.pyplot as plt

import librosa 


from STFT import create_sftf


def main():

    
    data = scipy.io.loadmat(r"DataSet\G1D1D2\G1D1.mat")

    sa = data["Sa"]    
    
    create_sftf(sa[0,0])
    

    x = 0
    pass 


if __name__ == "__main__":
    main()
