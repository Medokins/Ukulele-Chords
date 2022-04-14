import numpy as np
from scipy.fft import *
from scipy.io import wavfile


def freq(file, start_time, end_time):
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    dataToRead = data[int(start_time * sr / 1000) : int(end_time * sr / 1000) + 1]

    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq

print(freq("wav_music/Meltt - Only In Your Eyes.wav", 0, 1000))