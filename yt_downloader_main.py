###############
# YT DOWNLOADER
# DATE : 31 JULY 2025
# MADE : RUDY LETI
###############

import os
import re
import time
import urllib.request

import ffmpeg # pip install ffmpeg-python  +  Download : https://ffmpeg.org/download.html
from yt_dlp import YoutubeDL # pip install yt-dlp


art = r"""
__  ________  ___                  __             __       
\ \/ /_  __/ / _ \___ _    _____  / /__  ___ ____/ /__ ____
 \  / / /   / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
 /_/ /_/   /____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/   
"""

temp_audio_file = "temp_audio.webm"
temp_video_file = "temp_video.mp4"

def Parser(url:str,quality:int):
    format_selector = "bestvideo[height<=720][ext=mp4]+bestaudio[ext=webm]/mp4"
    
    if quality == 1:
        format_selector = "bestvideo[ext=mp4]+bestaudio[ext=webm]/mp4"

    ydl_opts = {
        "format": format_selector,
        "outtmpl": temp_video_file,
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as yt_video:
        print("\rExtracting video info...", end="")
        info_dict = yt_video.extract_info(url, download=False)
        
        if quality == 1:
            video_url = info_dict["requested_formats"][0]["url"]
            audio_url = info_dict["requested_formats"][1]["url"]
        elif quality == 2:
            video_url = info_dict["formats"][30]["url"]
            audio_url = info_dict["formats"][6]["url"]
            
        raw_title = f"{info_dict['title'].strip()} - {info_dict['uploader'].strip()}"
        sanitized_title = re.sub(r'[\\/*?:"<>|]',"", raw_title)
        output_path = f"{sanitized_title}.mp4"
        print("...Extraction complete.")
        return video_url, audio_url, output_path, yt_video


def DownLoader(video_url : str, audio_url: str, output_path: str, yt_video: YoutubeDL):
    try:
        print("\rDownloading Video...", end="")
        yt_video.download(video_url)
        print("Video Downloaded.")
        
        print("\rDownloading Audio...", end="")
        urllib.request.urlretrieve(url=audio_url, filename=temp_audio_file)
        print("...Audio Downloaded.")
        
        video_stream = ffmpeg.input(temp_video_file)
        audio_stream = ffmpeg.input(temp_audio_file)
        
        print("\rMerging Audio and Video...", end="")
        ffmpeg.output(video_stream, audio_stream, output_path, vcodec='libx264', acodec="aac").run(overwrite_output=True, quiet=True)
        print("...Merge complete.")
        BarLoader()
        print(f" - Successfully saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred during download or merge: {e}")
    finally:
        # CLEAN UP TEMPORARY FILES
        if os.path.exists(temp_video_file):
            os.remove(temp_video_file)
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)

def BarLoader():
    size = 40
    for i in range(1,101):
        blocs = int(i * size / 100)
        bar  = "█"* blocs + "_" * (size-blocs)
        print(f"\r[{bar}] {i}%", end="", flush=True)
        time.sleep(0.015)

# --------- main ---------
print(art)
url = input("Type or copy/paste the Youtube url you want: ")
if "https://www.youtube.com/watch?v=" not in url:
    raise ValueError

quality = int(input("Choose the quality of the video - 1)Best Quality or 2)Low Quality: "))

if isinstance(quality, int) == False:
    raise TypeError

if 1 > quality > 2:
    quality = 2

data = Parser(url,quality)
DownLoader(data[0],data[1],data[2],data[3])
