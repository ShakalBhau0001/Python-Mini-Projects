import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from pathlib import Path
import textwrap
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def generate_pdf(txt_file_path):
    try:
        txt_path = Path(txt_file_path)
        pdf_file = txt_path.with_suffix(".pdf")
        temp_pdf = txt_path.with_name("temp_content.pdf")
        c = canvas.Canvas(str(temp_pdf), pagesize=A4)
        width, height = A4
        font_size = 11
        line_height = 14
        toc = []
        y = height - inch
        
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if not line:
                    y -= line_height
                    continue
                if y <= inch:
                    c.setFont("Helvetica", 9)
                    c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")
                    c.showPage()
                    y = height - inch
                if line.strip().startswith(tuple(f"{i}." for i in range(1, 100))):
                    c.setFont("Courier-Bold", font_size)
                    c.setFillColor(colors.darkblue)
                    toc.append((line.strip(), c.getPageNumber() + 1))
                else:
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(colors.black)
                wrapped_lines = textwrap.wrap(line, width=90)
                for wline in wrapped_lines:
                    if y <= inch:
                        c.setFont("Helvetica", 9)
                        c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")
                        c.showPage()
                        y = height - inch
                        c.setFont("Helvetica", font_size)
                    c.drawString(inch, y, wline)
                    y -= line_height

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.black)
        c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")
        c.save()
        packet = BytesIO()
        toc_canvas = canvas.Canvas(packet, pagesize=A4)
        y = height - inch
        toc_canvas.setFont("Helvetica-Bold", 18)
        toc_canvas.setFillColor(colors.darkred)
        toc_canvas.drawCentredString(width / 2, y, "TABLE OF CONTENTS")
        y -= 40
        toc_canvas.setFont("Helvetica", 12)
        toc_canvas.setFillColor(colors.black)
        
        for cmd, page in toc:
            if y <= inch:
                toc_canvas.showPage()
                y = height - inch
            toc_canvas.drawString(inch, y, f"{cmd} ...... Page {page}")
            y -= 14
        toc_canvas.save()
        
        packet.seek(0)
        toc_reader = PdfReader(packet)
        content_reader = PdfReader(str(temp_pdf))
        writer = PdfWriter()

        for page in toc_reader.pages:
            writer.add_page(page)
        for page in content_reader.pages:
            writer.add_page(page)

        with open(pdf_file, "wb") as out_file:
            writer.write(out_file)

        temp_pdf.unlink(missing_ok=True)
        messagebox.showinfo("Success ✅", f"PDF created successfully:\n{pdf_file}")

    except Exception as e:
        messagebox.showerror("Error ❌", f"Something went wrong:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select TXT file",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        generate_pdf(file_path)

root = tk.Tk()
root.title("TXT To PDF Converter")
root.geometry("380x220")
root.resizable(False, False)
root.configure(bg="cyan")

label = tk.Label(
    root,
    text="Select a .txt file to generate a formatted PDF",
    font=("Helvetica", 13, "bold"),
    bg="cyan",
    fg="#222"
)
label.pack(pady=40)

btn = tk.Button(
    root,
    text="Select .txt & Generate PDF",
    font=("Helvetica", 12, "bold"),
    bg="red",
    fg="white",
    activebackground="#2748b3",
    activeforeground="cyan",
    padx=20,
    pady=8,
    command=select_file,
    relief="raised",
    bd=3
)
btn.pack(pady=10)
root.mainloop()
