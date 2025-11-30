# 🎵 YouTube Audio Downloader (Tkinter + yt-dlp)

This is a simple GUI-based YouTube Audio Downloader built using Python’s
tkinter library and yt-dlp. It allows users to easily download audio
(MP3) from any YouTube video with just one click.

---

## ✨ Features

- Download audio (MP3) from YouTube
- Simple and clean Tkinter GUI
- One-click MP3 download button
- Automatic audio extraction using FFmpeg
- Shows success and error messages

---

## 📁 Project Structure

```
YouTube-Audio-Downloader/
│── audio_downloader.py
└── README.md
```

---

## 🛠 Requirements

### 1️⃣ Install yt-dlp

```bash
pip install -U yt-dlp
```

### 2️⃣ Install FFmpeg

You can install FFmpeg using **two methods**: Manual download or Chocolatey.

---

### **Method 1: Manual Download**

1. Download FFmpeg (Essentials build):  
   https://www.gyan.dev/ffmpeg/builds/

2. Extract the ZIP to:
```
C:\ffmpeg\
```

3. Add FFmpeg to your PATH:
```
C:\ffmpeg\bin
```

4. Verify installation:
```bash
ffmpeg -version
```

---

### **Method 2: Install via Chocolatey**

1. Open **PowerShell as Administrator** (Right click → Run as Administrator)

2. Run the command:
```powershell
choco install ffmpeg-full -y
```

3. Wait for the download and installation to complete.

4. Verify installation:
```powershell
ffmpeg -version
```

> ⚠️ Note: Chocolatey automatically adds FFmpeg to your PATH.  
> If using `choco install ffmpeg` (lightweight version), the commands are the same.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ShakalBhau0001/Python-Mini-Projects.git
cd Python-Mini-Projects/YouTube-Audio-Downloader
```

### 2. Run the Script

```bash
python audio_downloader.py
```

### 3. Use the App
- Enter any **valid YouTube URL**
- Click **Download**
- File will save automatically
- Success or error message will appear

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Download videos only if you have rights or permission.

---

## ❤️ Developed By
Made with ❤️ using **Python** + **Tkinter** + **yt-dlp** + **FFmpeg**

---
