###############
# YT DOWNLOADER
# DATE : 31 JULY 2025"for
# MADE : RUDY LETI
###############

import os
import re
import time
import urllib.request
from pprint import pprint

import ffmpeg # pip install ffmpeg-python  +  Download : https://ffmpeg.org/download.html
from yt_dlp import YoutubeDL # pip install yt-dlp


art = r"""
__  ________  ___                  __             __       
\ \/ /_  __/ / _ \___ _    _____  / /__  ___ ____/ /__ ____
 \  / / /   / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
 /_/ /_/   /____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/   
"""

temp_audio_file = "temp/temp_audio.webm"
temp_video_file = "temp/temp_video.mp4"


def collect_resolutions(url:str) -> tuple:
    format_selector = "bestvideo[ext=mp4]+bestaudio[ext=webm]/best"
    ydl_opts = {
        "format": format_selector,
        "outtmpl": temp_video_file,
        "quiet": True,
        }
    with YoutubeDL(ydl_opts) as yt_video:
        info_dict = yt_video.extract_info(url, download=False)
        formats = info_dict.get("formats", [])
        resolutions = set()
        for n in formats:
            if n.get("video_ext",str) == "mp4" and n["height"] >= 480 and n.get("protocol",str) == "https":
                resolutions.add(n["height"])
    return sorted(resolutions),yt_video

def parse_video_info(url:str,user_choice:int,yt_video:YoutubeDL) -> tuple:
    print("\rExtracting video info...\n", end="")
    info_dict = yt_video.extract_info(url, download=False)
    raw_title = f"{info_dict['title'].strip()} - {info_dict['uploader'].strip()}"
    sanitized_title = re.sub(r'[\\/*?:"<>|]',"", raw_title)
    output_path = f"{sanitized_title}.mp4"
    yt_video.close()
    return output_path,info_dict

def filter_quality(info_dict:dict,user_choice:int) -> tuple:
    formats = info_dict.get("formats", [])
    v_urls = []
    a_urls = []
    count = 0
    print("Choose your video quality by typing the reference number:\n")
    for n in formats:
        if n.get("video_ext",str) == "mp4" and n["height"] == user_choice and n.get("protocol",str) == "https":
            print(f"{count} - format: {n.get("format_note",str)}")
            url = n.get("url",str)
            v_urls.append(url)
            count += 1
    for n in formats:
        if n.get("audio_ext",str) == "webm" and n.get("format_note",str) == "low":
            url = n.get("url",str)
            a_urls.append(url)
    return v_urls,a_urls[-1]

def download_and_merge(video_url : str, audio_url: str, output_path: str, yt_video: YoutubeDL):
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
        barLoader()
        print(f"\nSuccessfully saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred during download or merge: {e}")
    finally:
        # CLEAN UP TEMPORARY FILES
        if os.path.exists(temp_video_file):
            os.remove(temp_video_file)
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)

def barLoader():
    size = 40
    for i in range(1,101):
        blocs = int(i * size / 100)
        bar  = "█"* blocs + "_" * (size-blocs)
        print(f"\r[{bar}] {i}%", end="", flush=True)
        time.sleep(0.015)


if __name__ == "__main__":
    print(art)
    url = input("Type or copy/paste the Youtube url you want: ")
    resolutions = collect_resolutions((url))
    chosen_quality = int(input(f"Choose your video quality, {resolutions[0]}: "))
    data = parse_video_info(url,resolutions[1])
    filtred_data = filter_quality(data[1],chosen_quality)
    user_choice = int(input("\nMake your choice:"))
    
    if user_choice > len(filtred_data[0])-1 or user_choice < 0:
        raise ValueError(f"PLEASE TYPE A NUMBER BETWEEN 0 AND {len(filtred_data[0])-1}")
    
    download_and_merge(filtred_data[0][user_choice],filtred_data[1],data[0],resolutions[1])
    