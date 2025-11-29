import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "0.0%")
        root.title(f"Downloading... {percent}")
    elif d["status"] == "finished":
        root.title("YouTube Downloader")


def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return

    # Ask user for download folder
    download_folder = filedialog.askdirectory(title="Select Download Folder")
    if not download_folder:
        messagebox.showerror("Error", "Please select a folder to save the video")
        return

    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{download_folder}/%(title)s.%(ext)s",
            "noplaylist": True,
            "progress_hooks": [progress_hook],
            "extractor_args": {
                "youtube": {"player_client": ["web", "android", "web_safari"]}
            },
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Download completed!")

    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{e}")


root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x150")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", width=20, command=download_video)
download_button.pack(pady=15)

root.mainloop()
