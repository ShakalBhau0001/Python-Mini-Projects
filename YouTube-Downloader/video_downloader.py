import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    
    try:
        ydl_opts = {'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

root.mainloop()
