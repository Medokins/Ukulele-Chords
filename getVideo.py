from random import vonmisesvariate
import youtube_dl
import subprocess

def downloadVideo(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"Download complete... {filename}")

def convertToWav(mp3_file_name, wav_output_name):
    subprocess.call(['ffmpeg', '-i', mp3_file_name + ".mp3", wav_output_name + ".wav"])

convertToWav("music/Meltt - Only In Your Eyes", "wav_music/Meltt - Only In Your Eyes")