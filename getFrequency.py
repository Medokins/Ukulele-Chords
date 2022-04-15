import numpy as np
from scipy.fft import *
from scipy.io import wavfile

def freq(file, start_time, end_time):
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    dataToRead = data[int(start_time * sr) : int(end_time * sr) + 1]

    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)
    
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq
