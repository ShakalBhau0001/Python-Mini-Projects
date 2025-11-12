# 📄 PDF Convertor — TXT to PDF with Table of Contents

A simple yet elegant GUI tool to **convert any `.TXT` file into a well-formatted PDF** (with a **Table of Contents**) using **Python, Tkinter, and ReportLab**.  
Built with ❤️ by **[ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ✨ Features

- 🖱️ Easy-to-use graphical interface (Tkinter)
- 📘 Automatically generates **Table of Contents**
- 📄 Supports **multi-page PDFs** with proper page numbers
- 💬 Text wrapping for long lines
- 🎨 Clean design and optimized window layout
- 💥 Bold & colored headings detection (like `1.`, `2.` etc.)

---

## 📂 Project Structure

```bash
Txt-To-PDF-Generator/
│
├── txt_to_pdf_generator.py   # Main application
├── README.md                 # Project documentation
```

---

## 🧰 Requirements

Make sure you have **Python 3.7+** installed.

Install the required library using pip:

```bash
pip install reportlab
pip install pypdf
pip install PyPDF2
```

---

## 🚀 Usage

1. Clone or download this repository:

   ```bash
   git clone https://github.com/ShakalBhau0001/Python-Mini-Projects.git
   cd Txt-To-PDF-Generator
   
   ```

2. Run the Python script:

   ```bash
   python txt_to_pdf_generator.py
   ```

4. A GUI window will open — click **“Select .TXT & Generate PDF”**  
   Choose any `.txt` file and the app will create a **formatted PDF** in the same directory.

---

## 🧠 How It Works

- Reads your `.txt` file line by line.
- Automatically detects numbered headings (`1.`, `2.` …) and adds them to the **Table of Contents**.
- Adds page numbers to each page.
- Generates a new `.pdf` file in the same folder.

---


## 🧑‍💻 Author

**👤 ShakalBhau0001**  

---

## ⚙️ Tech Stack

- **Python 3**
- **Tkinter** — GUI Interface  
- **ReportLab** — PDF Generation  
- **Pathlib** — File Handling  

---

> 💬 _"A small idea beautifully executed can save hours of manual formatting."_

---
