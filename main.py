import pyaudio
import wave
import numpy as np

chunk = 2048

wf = wave.open('wav_music/Meltt - Only In Your Eyes.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
window = np.blackman(chunk)
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(swidth),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)

data = wf.readframes(chunk)

print(len(data))
print(chunk*swidth)

while len(data) == chunk*swidth*2:
    stream.write(data)
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data*2))*window
    fftData=abs(np.fft.rfft(indata))**2
    which = fftData[1:].argmax() + 1
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        thefreq = (which+x1)*RATE/chunk
        print("The freq is %f Hz.") % (thefreq)
    else:
        thefreq = which*RATE/chunk
        print("The freq is %f Hz.") % (thefreq)
    data = wf.readframes(chunk)
if data:
    stream.write(data)

stream.close()
p.terminate()