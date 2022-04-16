import youtube_dl
import subprocess

def downloadVideo(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    filename = filename.replace(":", "")
    duration = video_info['duration']
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl': f"music/{filename}",
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return filename, duration

def convertToWav(mp3_file_name, wav_output_name):
    subprocess.call(['ffmpeg', '-i', mp3_file_name, wav_output_name.replace(".mp3", "") + ".wav"])