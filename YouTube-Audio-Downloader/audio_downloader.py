import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", f"Video download failed:\n{e}")

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Audio downloaded as MP3!")
    except Exception as e:
        messagebox.showerror("Download Error", f"Audio download failed:\n{e}")

root = tk.Tk()
root.title("YouTube Audio/Video Downloader")
root.geometry("400x200")
root.resizable(False, False)
tk.Label(root, text="Enter YouTube URL: ⬇️").pack(pady=10)
url_entry = tk.Entry(root, width=55)
url_entry.pack(pady=5)
video_btn = tk.Button(root, text="Download Video 🎥", command=download_video, width=30, bg="skyblue")
video_btn.pack(pady=10)
audio_btn = tk.Button(root, text="Download Audio 🎵", command=download_audio, width=30, bg="lightgreen")
audio_btn.pack(pady=5)

root.mainloop()
