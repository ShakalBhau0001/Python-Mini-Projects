# 🎥🎵 YouTube Audio/Video Downloader (Tkinter + yt-dlp)

A simple yet powerful GUI-based **YouTube Downloader** built with Python’s `tkinter` for the interface and `yt-dlp` for downloading content.  
This tool allows you to download both **videos** 🎬 and **audio (MP3)** 🎵 directly from YouTube in just a few clicks.

---

## ✨ Features
- Download **YouTube videos** in the best available quality 🎥  
- Download **audio only (MP3)** with automatic conversion 🎵  
- User-friendly **GUI interface**  
- Error handling for invalid or empty URLs  
- Saves files in the **current working directory**  

---

## 📂 Project Structure
```
YouTube-Audio-Downloader/
│── audio_downloader.py     # Main program file
│── README.md               # Project documentation
```

---

## 🛠️ Requirements
Make sure you have the following installed:

```bash
pip install yt-dlp
```

⚡ For **audio extraction (MP3)**, you also need **FFmpeg**:  
- [Download FFmpeg](https://ffmpeg.org/download.html)  
- Ensure `ffmpeg` is added to your system PATH.  

---

## 🚀 How to Run
1. Clone the repository or copy this project to your local machine.  
2. Install the required dependency (`yt-dlp`).  
3. (Optional) Install **FFmpeg** for audio conversion.  
4. Run the script:  

```bash
python audio_downloader.py
```

5. Paste a valid YouTube URL in the input box.  
6. Click **Download Video 🎥** or **Download Audio 🎵**.  

---

## ⚠️ Disclaimer
This tool is for **educational purposes only**. Download content only if you have the rights or permission.  

---

💻 Developed with ❤️ using Python + Tkinter + yt-dlp
