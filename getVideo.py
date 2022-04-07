import pafy
import vlc
import time

url = "https://www.youtube.com/watch?v=Yd5pYNxBhHg"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
length = int(video.duration.split(":")[0]) * 3600 + int(video.duration.split(":")[1]) * 60 + int(video.duration.split(":")[2])

media.play()
time.sleep(length + 5)