import speech_recognition as sr
import youtube_dl

from pydub import AudioSegment #WAV conversion

import os



a=input("enter url ")

ydl_opts = {
    'format': 'bestaudio/best',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if not os.path.exists('podcasts'):
    os.mkdir('podcasts')
else:
    os.chdir('podcasts')

#download podcasts:
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([a])
except youtube_dl.DownloadError as e:
    print(e)


