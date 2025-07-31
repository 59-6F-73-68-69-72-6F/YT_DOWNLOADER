# YT Downloader⏬

A simple and efficient command-line tool to download YouTube videos directly to your computer.

 <!-- You can replace this with a real screenshot -->

## Description

This Python script provides a straightforward way to download any YouTube video. It prompts the user for a video URL and a quality preference, then handles the entire process of downloading the video and audio streams, merging them into a single high-quality MP4 file, and saving it locally.

## Features

*   **Easy to Use**: Simple command-line interface.
*   **Quality Selection**: Choose between the best available quality or a lower resolution (720p) to save disk space.
*   **Automatic Merging**: Downloads video and audio separately and uses FFmpeg to merge them into a complete video file.
*   **Smart Naming**: Automatically names the final file using the video's title and the uploader's name (e.g., `Video Title - Uploader Name.mp4`).
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
    *   After downloading, ensure the `ffmpeg` executable is available in your system's PATH.

## How to Use

1.  Open your terminal or command prompt.
2.  Navigate to the directory where `yt_downloader_main.py` is located.
3.  Run the script with the command: `python yt_downloader_main.py`
4.  When prompted, paste the full YouTube video URL and press **Enter**.
5.  Choose your desired quality by typing `1` for Best Quality or `2` for Low Quality, then press **Enter**.
6.  Wait for the script to finish. The final `.mp4` file will be saved in the same directory.
