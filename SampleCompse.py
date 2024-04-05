
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from PyEMD.EMD2d import EMD2D  #, BEMD



def decompose_stft(stft):
    

    emd2d = EMD2D()  # BEMD() also works
    IMFs_2D = emd2d(stft)
        
    x = 0

    pass  






