import numpy as np
from aubio import source, pitch

#most of this is sample code from aubio
start_time = 1000
end_time = 1010
samplerate = 48000

s = source("wav_music\Meltt - Only In Your Eyes.wav", samplerate, start_time)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", end_time, start_time, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []

total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitches += [pitch]
    confidence = pitch_o.get_confidence()
    confidences += [confidence]
    total_frames += read
    if read < start_time: break

print("Average frequency = " + str(np.array(pitches).mean()) + " hz")
