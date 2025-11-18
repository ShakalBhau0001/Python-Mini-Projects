import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def calculate_ymd_diff(d1, d2):
    if d2 < d1:
        d1, d2 = d2, d1  

    y1, m1, day1 = d1.year, d1.month, d1.day
    y2, m2, day2 = d2.year, d2.month, d2.day

    years = y2 - y1
    months = m2 - m1
    days = day2 - day1

    if days < 0:
        prev_month = m2 - 1 if m2 > 1 else 12
        prev_year = y2 if m2 > 1 else y2 - 1

        days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) -
                              datetime(prev_year, prev_month, 1)).days

        days += days_in_prev_month
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except:
        messagebox.showerror("Error", "Enter date as DD-MM-YYYY")
        return None


def calculate_difference():
    d1 = parse_date(date1_entry.get())
    d2 = parse_date(date2_entry.get())
    if d1 is None or d2 is None:
        return

    years, months, days = calculate_ymd_diff(d1, d2)

    result_label.config(
        text=f"Years: {years}\nMonths: {months}\nDays: {days}"
    )


root = tk.Tk()
root.title("Date Calculator")
root.geometry("400x250")
ttk.Label(root, text="Date 1 (DD-MM-YYYY)").pack()
date1_entry = ttk.Entry(root)
date1_entry.pack(pady=5)
ttk.Label(root, text="Date 2 (DD-MM-YYYY)").pack()
date2_entry = ttk.Entry(root)
date2_entry.pack(pady=5)
ttk.Button(root, text="Calculate Difference", command=calculate_difference).pack(pady=10)
result_label = ttk.Label(root, text="", font=("Segoe UI", 12))
result_label.pack(pady=20)

root.mainloop()
