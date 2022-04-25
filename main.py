import librosa
import numpy as np
from getFrequency import freq
from getVideo import downloadVideo, convertToWav
from frequencyConverter import frequency_to_note
from createImage import joinHorizontal, joinVertical, cutChords

name = "twenty one pilots House of Gold [OFFICIAL VIDEO]" #if You want to get chords from an existing file
url = "https://www.youtube.com/watch?v=mDyxykpYeu8&ab_channel=FueledByRamen"
frequency_table = []
chords = []

step = 1

if (len(url) > 0 and len(name) == 0):
    name, length = downloadVideo(url)
    convertToWav(f"music/{name}", f"wav_music/{name}")
    name = name.replace(".mp3", "")
    name = f"wav_music/{name}.wav"
else:
    name = f"wav_music/{name}.wav" 
    length = librosa.get_duration(filename=name)

for i in np.arange(0, int(length) - 1, step):
    frequency = freq(name, i, i+ step)
    frequency_table.append(frequency)
    chords.append(frequency_to_note(frequency))

#najpier pociac chords na 6-akrodowe wiersze i je wrzucic do tego co nizej

chordsList = cutChords(chords, 6)

for i in range(len(chordsList)):
    joinHorizontal([i], i)

joinVertical(chordsList, name)