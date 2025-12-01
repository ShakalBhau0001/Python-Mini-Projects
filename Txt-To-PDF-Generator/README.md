# 📄 PDF Convertor — TXT to PDF with Table of Contents

A simple yet elegant GUI tool to **convert any `.TXT` file into a well-formatted PDF** (with a **Table of Contents**) using **Python, Tkinter, and ReportLab**.  

---

## ✨ Features

- 🖱️ Easy-to-use graphical interface (Tkinter)
- 📘 Automatically generates **Table of Contents**
- 📄 Supports **multi-page PDFs** with proper page numbers
- 💬 Text wrapping for long lines
- 🎨 Clean design and optimized window layout
- 💥 Bold & colored headings detection (like `1.`, `2.` etc.)
- 📝 Supports emojis and UTF-8 symbols (if `DejaVuSans.ttf` is available)

---

## 📂 Project Structure

```bash
Txt-To-PDF-Generator/
│
├── txt_to_pdf_generator.py   # Main application
├── DejaVuSans.ttf            # Optional for emoji support
└── README.md                 # Project documentation
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
> Note: The code optionally uses `DejaVuSans.ttf` for emojis.
> If this font is missing, it falls back to **Helvetica**, which may not display emojis correctly.

---

## 🚀 Usage

1. Clone or download this repository:

   ```bash
   git clone https://github.com/ShakalBhau0001/Python-Mini-Projects.git
   cd Txt-To-PDF-Generator
   
   ```
2. Make sure `DejaVuSans.ttf` is in the same folder as the script (optional for emoji support).

3. Run the Python script:

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
- If `DejaVuSans.ttf` is present, emojis and UTF-8 symbols are displayed correctly.

---


## 🧑‍💻 Author

Built with ❤️ by **[ShakalBhau0001](https://github.com/ShakalBhau0001)** 

---

## ⚙️ Tech Stack

- **Python 3**
- **Tkinter** — GUI Interface  
- **ReportLab** — PDF Generation  
- **Pathlib** — File Handling
- **PyPDF2** — PDF Manipulation

---

> 💬 _"A small idea beautifully executed can save hours of manual formatting."_

---
