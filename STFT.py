


import librosa 
import scipy 
import mne
import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import butter, lfilter, freqz

def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    w, h = freqz(b, a, fs=fs, worN=2000)
    # plt.plot(w, np.abs(h))
    return y

def bandbass_filter(data, fs, lowcut, highcut):
    
    filter_data = data.copy()
    filter_data = butter_bandpass_filter(filter_data, lowcut, highcut, fs, order=2)
    return filter_data


def preprocess(signal, sr):
    
    fs = 250
    
    new_signals = []
    for x in signal[:]:
        new_signal = librosa.resample(y=x, orig_sr=sr, target_sr=250)  
        new_signals.append(new_signal)
      
    filtered_signal = bandbass_filter(new_signal, fs=fs, lowcut=2, highcut=30)
    
    return filtered_signal


def create_sftf( signal, gain=0 ):
    
    # 250hz 
    # 
    # scipy.signal.resample(signal, orig_sr=1000, target_sr=250)
    fs = 250 
    # ch_names = [str(x) for x in range(new_signal.shape[0])]
    # info = mne.create_info(ch_names, fs, ch_types='eeg', verbose=None)
    # t = mne.EvokedArray(new_signal, info)
    # new_signal = mne.set_eeg_reference(t)
    
    filtered_signal = preprocess(signal, 1000)
    stft = librosa.stft(y=filtered_signal, n_fft=512, hop_length=100, win_length=250)
    spectrograms = np.abs(stft)**2
    # d,t,s = scipy.signal.stft(new_signal, fs = 250)
    return stft, spectrograms
    
     