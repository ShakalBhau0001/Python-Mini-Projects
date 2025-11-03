# 🧮 Scientific Calculator (Tkinter GUI)

A fully functional, theme-switchable **Scientific Calculator** built
using **Python's Tkinter** library.\
It supports **arithmetic**, **scientific**, and **memory-based
operations** with a responsive and intuitive interface.

------------------------------------------------------------------------

## ⚙️ Features

-   🎨 **Light/Dark Theme** toggle (instant switch)
-   🧮 **Scientific Functions**: sin, cos, tan, log, sqrt, powers, etc.
-   💾 **Memory Functions**:
    -   `M+` → Add to memory\
    -   `M−` → Subtract from memory\
    -   `MR` → Recall memory
-   🧠 **History Log** --- Automatically saves last 10 calculations
-   ⌨️ **Keyboard Shortcuts** for fast operation
-   🧰 **Smart Input Handling** --- Auto-balances parentheses and
    sanitizes expressions
-   💥 **Error Handling** --- Prevents invalid evaluations and protects
    against code injection

------------------------------------------------------------------------

## 📂 Project Structure

```bash
Scientific-Calculator/
│
├── scientific_calculator.py    # Main application
├── README.md                   # Project documentation
```

------------------------------------------------------------------------

## 🧠 How It Works

1.  **Input Capture:**\
    Expressions are built character-by-character using buttons or
    keyboard input.

2.  **Sanitization & Conversion:**\
    The `_sanitize_and_prepare()` method translates user symbols (`√`,
    `^`, `log`) into safe Python equivalents like `math.sqrt`, `**`, and
    `math.log10`.

3.  **Secure Evaluation:**\
    The expression is evaluated using a restricted environment with only
    `math` functions accessible --- protecting from unsafe code
    execution.

4.  **Output Display:**\
    Results are displayed instantly and added to history (up to 10
    latest entries).

------------------------------------------------------------------------

## ⚙️ Installation & Run

### Prerequisites

-   **Python 3.8+**
-   Tkinter (comes pre-installed with Python)

### Steps

``` bash
# Clone or copy the script
git clone https://github.com/ShakalBhau0001/Python-Mini-Projects.git
cd scientific-calculator

# Run the application
python scientific_calculator.py
```

------------------------------------------------------------------------

## 🪄 Future Improvements

-   Add **exponential and factorial** functions\
-   Include **graph plotting** (using Matplotlib)\
-   Implement **angle mode toggle** (degrees ↔ radians)\
-   Save full history to file

------------------------------------------------------------------------

## 🖋️ Author

**Developed by:** ShakalBhau0001
Built with 💙 using **Python Tkinter**, for those who love clean UI and
smooth functionality.

------------------------------------------------------------------------

## 🧾 License

This project is released under the **MIT License**.\
You are free to modify, distribute, and use it for personal or
educational purposes.

------------------------------------------------------------------------

> *"Precision meets simplicity --- a calculator that feels alive."*
