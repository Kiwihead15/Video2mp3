import os
import sys

import yt_dlp

OUTPUT_DIR = "new_songs"


def download_mp3(url: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "output")
        return os.path.join(OUTPUT_DIR, f"{title}.mp3")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python video2mp3.py <youtube_url>")
        sys.exit(1)

    try:
        output = download_mp3(sys.argv[1])
        print(f"Saved: {output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
