# YT Downloader⏬

A simple and efficient command-line tool to download YouTube videos directly to your computer in your desired resolution.

<img width="619" height="173" alt="image" src="https://github.com/user-attachments/assets/6f991fcd-d417-43c2-8888-0f3cd630249b" />


## Description

This Python script provides a straightforward way to download any YouTube video. It fetches all available resolutions, lets you choose one, and then downloads the highest quality video and audio for that resolution. It uses `yt-dlp` for fetching information and downloading, and `FFmpeg` to merge the video and audio streams into a single high-quality MP4 file.

## Features

*   **Easy to Use**: Simple command-line interface.
*   **Quality Selection**: Automatically lists available video resolutions (e.g., 480p, 720p, 1080p) for you to choose from.
*   **Format Selection**: If multiple formats are available for a resolution (e.g., different frame rates), you can pick the one you prefer.
*   **Automatic Merging**: Downloads video and audio separately and uses FFmpeg to merge them into a complete video file.
*   **Smart Naming**: Automatically names the final file using the video's title and the uploader's name (e.g., `Video Title - Uploader Name.mp4`), sanitizing it for compatibility with your filesystem.
*   **Clean Operation**: Temporary files created during the process are automatically deleted upon completion.
*   **Progress Indicators**: See the status of the download and merging process, complete with a final progress bar.

## Requirements

Before running the script, you need to have the following installed:

1.  **Python 3**
2.  **yt-dlp**: A powerful tool for downloading video/audio from thousands of sites.
    ```bash
    pip install yt-dlp
    ```
3.  **ffmpeg-python**: A Python wrapper for FFmpeg.
    ```bash
    pip install ffmpeg-python
    ```
4.  **FFmpeg**: The core multimedia framework for processing video and audio.
    *   **You must download FFmpeg separately** from the official website: https://ffmpeg.org/download.html

## How to Use

1.  Open your terminal or command prompt.
2.  Navigate to the directory where `yt_downloader_main.py` is located.
3.  Run the script with the command: `python yt_downloader_main.py`
4.  When prompted, paste the full YouTube video URL and press **Enter**.
5.  Choose your desired quality by typing `1` for Best Quality or `2` for Low Quality, then press **Enter**.
6.  Wait for the script to finish. The final `.mp4` file will be saved in the same directory.
