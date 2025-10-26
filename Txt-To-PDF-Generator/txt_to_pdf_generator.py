import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from pathlib import Path
import textwrap

# Generate PDF
def generate_pdf(txt_file_path):
    try:
        txt_path = Path(txt_file_path)
        pdf_file = txt_path.with_suffix(".pdf")
        c = canvas.Canvas(str(pdf_file), pagesize=A4)
        width, height = A4
        font_size = 11
        line_height = 14
        toc = []

        # Start drawing content
        y = height - inch
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if not line:
                    y -= line_height
                    continue

                # New page if bottom reached
                if y <= inch:
                    c.setFont("Helvetica", 9)
                    c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")
                    c.showPage()
                    y = height - inch

                # Check if heading (1., 2., 3. etc.)
                if line.strip().startswith(tuple(f"{i}." for i in range(1, 100))):
                    c.setFont("Courier-Bold", font_size)
                    c.setFillColor(colors.darkblue)
                    toc.append((line.strip(), c.getPageNumber()))
                else:
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(colors.black)

                # Wrap long lines
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

        # Add page number for last page
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.black)
        c.drawRightString(width - inch, 0.5 * inch, f"Page {c.getPageNumber()}")

        # Add Table of Contents
        c.showPage()
        y = height - inch
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(colors.darkred)
        c.drawCentredString(width / 2, y, "TABLE OF CONTENTS")
        y -= 40
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)

        for cmd, page in toc:
            if y <= inch:
                c.showPage()
                y = height - inch
            c.drawString(inch, y, f"{cmd} ...... Page {page}")
            y -= 14

        c.save()
        messagebox.showinfo("Success ✅", f"PDF created successfully:\n{pdf_file}")

    except Exception as e:
        messagebox.showerror("Error ❌", f"Something went wrong:\n{e}")

# File Selection Function
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select TXT file",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        generate_pdf(file_path)

# GUI Setup
root = tk.Tk()
root.title("📄 TXT To PDF Converter")
root.geometry("400x280")
root.resizable(False, False)
root.configure(bg="#f2f4f7")

# Title Label
label = tk.Label(
    root,
    text="Select a .txt file to generate a formatted PDF",
    font=("Helvetica", 13, "bold"),
    bg="#f2f4f7",
    fg="#222"
)
label.pack(pady=40)

# Button
btn = tk.Button(
    root,
    text="Select .txt & Generate PDF",
    font=("Helvetica", 12, "bold"),
    bg="#1e3a8a",
    fg="white",
    activebackground="#2748b3",
    activeforeground="white",
    padx=20,
    pady=8,
    command=select_file,
    relief="raised",
    bd=3
)
btn.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="© 2025 — ShakalBhau0001",
    font=("Helvetica", 9),
    bg="#f2f4f7",
    fg="#444"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
