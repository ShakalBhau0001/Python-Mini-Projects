import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import platform
import socket
import uuid
import psutil
import re
import json


# 🔍 Validate IPv4 Format
def validate_ip(ip):
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return bool(pattern.match(ip))


# 🌐 Fetch IP Information
def get_ip_info(ip_address):
    try:
        resp = requests.get(f"http://ipapi.co/{ip_address}/json", timeout=5)
        return resp.json()
    except Exception as e:
        return {"error": f"Failed to fetch IP info: {e}"}


# 💻 Get Local System / Device Info


def get_device_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # MAC address (correct byte order)
        mac_address = ":".join(
            ["{:02x}".format((uuid.getnode() >> i) & 0xFF) for i in range(40, -1, -8)]
        )

        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        return {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
            "Local IP": local_ip,
            "Hostname": hostname,
            "MAC Address": mac_address,
            "FQDN": socket.getfqdn(),
            "Uptime (Boot Time)": psutil.boot_time(),
            "Total RAM (GB)": f"{memory.total / (1024**3):.2f}",
            "RAM Used (%)": memory.percent,
            "Disk Total (GB)": f"{disk.total / (1024**3):.2f}",
            "Disk Used (%)": disk.percent,
        }
    except Exception as e:
        return {"error": f"Device info error: {e}"}


# 🖥 Display Combined Results


def show_info():
    ip_address = ip_entry.get().strip()

    if not validate_ip(ip_address):
        messagebox.showwarning("Invalid IP", "Please enter a valid IPv4 address.")
        return

    ip_info = get_ip_info(ip_address)
    if "error" in ip_info:
        messagebox.showerror("Lookup Error", ip_info["error"])
        return

    device_info = get_device_info()

    output = "\n📌 IP Information:\n"
    for k, v in ip_info.items():
        output += f"  {k}: {v}\n"

    output += "\n💻 Device Information:\n"
    for k, v in device_info.items():
        output += f"  {k}: {v}\n"

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)

    history_list.insert(tk.END, ip_address)


# 🧹 Clear Input & Output


def clear_info():
    ip_entry.delete(0, tk.END)
    output_text.delete(1.0, tk.END)


# 📤 Export Results to TXT / JSON


def export_info():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("JSON Files", "*.json")],
    )
    if not file_path:
        return

    content = output_text.get(1.0, tk.END).strip()

    # Convert to JSON
    if file_path.endswith(".json"):
        try:
            data_map = {}
            for line in content.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    data_map[k.strip()] = v.strip()

            content = json.dumps(data_map, indent=4)

        except Exception as e:
            messagebox.showerror("JSON Error", f"Export failed: {e}")
            return

    with open(file_path, "w") as f:
        f.write(content)

    messagebox.showinfo("Exported", f"File saved:\n{file_path}")


# 🎨 UI Setup

root = tk.Tk()
root.title("IP Address Tracker")
root.geometry("750x650")

style = ttk.Style()
style.theme_use("clam")

main = ttk.Frame(root, padding=10)
main.pack(fill="both", expand=True)

# Input Label + Entry
ttk.Label(main, text="Enter IP Address:", font=("Arial", 14)).grid(
    row=0, column=0, sticky="w"
)
ip_entry = ttk.Entry(main, width=30, font=("Arial", 14))
ip_entry.grid(row=0, column=1, padx=10, pady=5)

# Buttons
btn_frame = ttk.Frame(main)
btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

ttk.Button(btn_frame, text="Track IP", command=show_info).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Clear", command=clear_info).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Export", command=export_info).grid(row=0, column=2, padx=5)

# Output
output_text = tk.Text(main, wrap="word", width=70, height=22, font=("Arial", 12))
output_text.grid(row=2, column=0, columnspan=2, pady=10)

# History
ttk.Label(main, text="Search History:", font=("Arial", 14)).grid(
    row=3, column=0, sticky="w"
)
history_list = tk.Listbox(main, height=6, font=("Arial", 12))
history_list.grid(row=4, column=0, columnspan=2, sticky="we")

root.mainloop()
