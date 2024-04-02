


import librosa 
import scipy 

import matplotlib.pyplot as plt


def create_sftf( signal ):
    
    # 250hz 
    # 
    # scipy.signal.resample(signal, orig_sr=1000, target_sr=250)
    new_signal = librosa.resample(y=signal, orig_sr=1000, target_sr=250)
    
    # stft = librosa.stft(y=new_signal, n_fft= 1024, hop_length=100, win_length=50)
    d,t,s = scipy.signal.stft(new_signal, fs = 250)
    
    x = 0
    
     