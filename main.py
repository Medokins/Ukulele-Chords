import librosa
import numpy as np
from pathlib import Path
from getFrequency import freq
from getVideo import downloadVideo, convertToWav
from frequencyConverter import frequency_to_note
from createImage import joinHorizontal, joinVertical, cutChords

name = "twenty one pilots House of Gold [OFFICIAL VIDEO]" #if You want to get chords from an existing file
url = "https://www.youtube.com/watch?v=mDyxykpYeu8&ab_channel=FueledByRamen"
chords_in_row = 10
step = 2

frequency_table = []
chords = []

[f.unlink() for f in Path("tempChords").glob("*") if f.is_file()] 
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
    chords.append(frequency_to_note(frequency)[0])

chordsList = cutChords(chords, chords_in_row)
for _ in chordsList: print(_) 
for i in range(len(chordsList)): joinHorizontal(chordsList[i], i)

name = name.replace("wav_music/", "")
name = name.replace(".wav", "")

joinVertical(int(np.ceil(len(chords)/chords_in_row)), name)
[f.unlink() for f in Path("tempChords").glob("*") if f.is_file()] 