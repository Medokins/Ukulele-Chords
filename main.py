import librosa
from getFrequency import freq
from getVideo import downloadVideo, convertToWav
from frequencyConverter import frequency_to_note

name = "sanah i Dawid Podsiadło „ostatnia nadzieja”" #if You want to get chords from an existing file
url = "https://www.youtube.com/watch?v=mDyxykpYeu8&ab_channel=FueledByRamen"
frequency_table = []
chords = []

if (len(url) > 0 and len(name) == 0):
    name, length = downloadVideo(url)
    convertToWav(f"music/{name}", f"wav_music/{name}")
    name = name.replace(".mp3", "")
    name = f"wav_music/{name}.wav"
else:
    name = f"wav_music/{name}.wav" 
    length = librosa.get_duration(filename=name)

for i in range(int(length) - 1):
    frequency = freq(name, i, i+1)
    frequency_table.append(frequency)
    chords.append(frequency_to_note(frequency))

print(chords)