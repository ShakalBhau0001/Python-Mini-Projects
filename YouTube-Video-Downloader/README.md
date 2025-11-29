# 🎥 YouTube Video Downloader (Python + Tkinter + yt-dlp)

A lightweight and user-friendly **YouTube Video Downloader** built using Python’s `tkinter` GUI and the powerful `yt-dlp` engine.

---

## ✨ Features
- 📥 Download YouTube videos in **best available quality**
- 🎛 Simple & clean GUI interface
- ⚡ Fast & reliable downloads using yt-dlp
- 🛠 Error handling for invalid or empty URLs
- 💾 Saves videos in the current working directory
- 🔧 FFmpeg support for merging high-quality video + audio streams

---

## 📁 Project Structure

```
YouTube-Video-Downloader/
│
├── video_downloader.py
└── README.md
```

---

## 🛠 Prerequisites

### 1️⃣ Install yt-dlp

```bash
pip install -U yt-dlp
```

### 2️⃣ Install FFmpeg (Required for merging video/audio)

#### Windows FFmpeg Installation

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
cd Python-Mini-Projects/YouTube-Video-Downloader
```

### 2. Run the Script

```bash
python video_downloader.py
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
Made with ❤️ using **Python**, **Tkinter**, and **yt-dlp**

---
