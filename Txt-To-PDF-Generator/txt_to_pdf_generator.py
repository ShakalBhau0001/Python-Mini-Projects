import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.lib import colors
from pathlib import Path
import textwrap
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

try:
    pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))
    FONT_NAME = "DejaVu"
except Exception:
    FONT_NAME = "Helvetica"


def add_page_number(c, width):
    c.setFont(FONT_NAME, 10)
    c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")


def generate_pdf(txt_file_path):
    try:
        txt_path = Path(txt_file_path)
        pdf_file = txt_path.with_suffix(".pdf")
        temp_pdf = txt_path.with_name("temp_content.pdf")

        width, height = A4
        font_size = 11
        line_height = 15

        c = canvas.Canvas(str(temp_pdf), pagesize=A4)
        y = height - inch

        toc = []

        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if not line:
                    y -= line_height
                    continue
                if y <= inch:
                    add_page_number(c, width)
                    c.showPage()
                    y = height - inch
                if line.strip().startswith(tuple(f"{i}." for i in range(1, 999))):
                    c.setFont(FONT_NAME, font_size + 1)
                    c.setFillColor(colors.darkblue)
                    toc.append((line.strip(), c.getPageNumber() + 1))
                else:
                    c.setFont(FONT_NAME, font_size)
                    c.setFillColor(colors.black)
                wrapped = textwrap.wrap(line, width=90)
                for wline in wrapped:
                    if y <= inch:
                        add_page_number(c, width)
                        c.showPage()
                        y = height - inch
                    c.drawString(inch, y, wline)
                    y -= line_height

        add_page_number(c, width)
        c.save()

        packet = BytesIO()
        toc_canvas = canvas.Canvas(packet, pagesize=A4)
        y = height - inch

        toc_canvas.setFont(FONT_NAME, 20)
        toc_canvas.setFillColor(colors.darkred)
        toc_canvas.drawCentredString(width / 2, y, "📑 TABLE OF CONTENTS")
        y -= 40

        toc_canvas.setFont(FONT_NAME, 12)
        toc_canvas.setFillColor(colors.black)

        for title, page in toc:
            if y <= inch:
                toc_canvas.showPage()
                y = height - inch
            toc_canvas.drawString(inch, y, f"{title}  ..... Page {page}")
            y -= 18

        toc_canvas.save()
        packet.seek(0)

        toc_reader = PdfReader(packet)
        content_reader = PdfReader(str(temp_pdf))
        writer = PdfWriter()

        for p in toc_reader.pages:
            writer.add_page(p)
        for p in content_reader.pages:
            writer.add_page(p)

        with open(pdf_file, "wb") as out:
            writer.write(out)

        temp_pdf.unlink(missing_ok=True)
        messagebox.showinfo("Success 🥰", f"PDF created successfully:\n{pdf_file}")

    except Exception as e:
        messagebox.showerror("Error 😢", f"Something went wrong:\n{e}")


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select TXT File", filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        generate_pdf(file_path)


def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#222222")
        label.configure(bg="#222222", fg="white")
        btn.configure(bg="#ff4081", fg="white")
        mode_btn.configure(text="☀️", bg="#444", fg="white")
    else:
        root.configure(bg="#00e0ff")
        label.configure(bg="#00e0ff", fg="black")
        btn.configure(bg="#ff0040", fg="white")
        mode_btn.configure(text="🌙", bg="#ffe6e6", fg="black")


root = tk.Tk()
root.title("TXT → PDF Converter 📝➡️📄")
root.geometry("420x280")
root.resizable(False, False)

dark_mode = False
root.configure(bg="#00e0ff")

label = tk.Label(
    root,
    text="Select a .txt file to generate a PDF",
    font=(FONT_NAME, 12, "bold"),
    bg="#00e0ff",
    wraplength=360,
)
label.pack(pady=30)

btn = tk.Button(
    root,
    text="📄 Select .txt & Generate PDF",
    font=(FONT_NAME, 12, "bold"),
    bg="#ff0040",
    fg="white",
    padx=20,
    pady=10,
    relief="raised",
    bd=3,
    command=select_file,
)
btn.pack(pady=10)
mode_btn = tk.Button(
    root,
    text="🌙",
    font=(FONT_NAME, 11, "bold"),
    bg="#ffe6e6",
    fg="black",
    command=toggle_mode,
)
mode_btn.pack(pady=10)
root.mainloop()
