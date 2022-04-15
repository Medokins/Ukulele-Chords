import librosa
from getFrequency import freq
from getVideo import downloadVideo, convertToWav
from frequencyConverter import frequency_to_note

download = False
name = "Meltt - Only In Your Eyes"
url = ""
frequency_table = []
chords = []

if download:
    name, length = downloadVideo(url)
    convertToWav(f"music/{name}", f"wav_music/{name}")
    name = f"wav_music/{name}.wav"
else:
    name = f"wav_music/{name}.wav"
    length = librosa.get_duration(filename=name)

for i in range(int(length) - 1):
    frequency = freq(name, i, i+1)
    frequency_table.append(frequency)
    chords.append(frequency_to_note(frequency))

print(chords)