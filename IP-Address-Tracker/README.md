## 🌐 IP Address Tracker (Tkinter + Requests + psutil)

A **GUI-based IP Address Tracker** built with Python’s **Tkinter**, **Requests**, and **psutil** libraries.
This app allows you to easily fetch **IP information** and **detailed device stats**, maintain **search history**, and export results in **TXT** or **JSON** format.

---

## ✨ Features

- 🔍 Track any **valid IPv4 address**
- 🌎 Fetch IP location, ISP, and network details via **ipapi.co** API
- 💻 Collect **system/device information** (OS, CPU, RAM, disk usage, MAC address, hostname, uptime, etc.)
- 🗂 Maintain **search history** in the GUI
- 🧹 Clear input/output with a single click
- 📤 Export results as **TXT** or **JSON** files
- ✅ Modern and responsive **Tkinter GUI**

---

## 📁 Project Structure

```bash
IP-Address-Tracker/
│── ip_address_tracker.py
└── README.md
```

---

## 🛠 Requirements

Install the required Python libraries:
```bash
pip install requests psutil
```

> Note: `tkinter`, `platform`, `socket`, `uuid`, and `re` are included in standard Python installations.

 ---

 ## 🚀 How to Run
 
**1️⃣ Clone the Repository**
```bash
git clone https://github.com/ShakalBhau0001/Python-Mini-Projects.git
cd IP-Address-Tracker
```

**2️⃣ Run the Script**
```bash
python ip_address_tracker.py
```

---

## 🖥 How to Use

1. Enter a **valid IPv4 address** in the input field
2. Click **Track IP** to fetch IP and device information
3. View the results in the **output box**
4. Save the results by clicking **Export as TXT or JSON**
5. Use **Clear** to reset the input and output
6. Previous IP queries are stored in the **Search History** panel

---

## 📌 Key Technologies Used

- **Tkinter** → GUI interface
- **Requests** → Fetch IP data from ipapi.co
- **psutil** → System info (RAM, disk usage, uptime)
- **UUID** + **Socket** → MAC address, hostname, and network info
- **Regex** → Validate IPv4 addresses

---

## ⚠️ Notes & Limitations

- Requires an **active internet connection** for IP lookups
- Works only for **IPv4 addresses**
- API used: ipapi.co(free tier may have rate limits)
- Device/system information is **collected locally** and not sent online

---

## ❤️ Developed By ShakalBhau0001

Made with ❤️ using **Python** + **Tkinter** + **Requests** + **psutil**

---
