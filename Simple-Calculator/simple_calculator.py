import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("460x460")
        self.root.configure(bg="#f0f0f0")
        self.expression = ""
        self.input_text = tk.StringVar()
        input_frame = tk.Frame(self.root, bd=0, relief=tk.RIDGE, bg="#f0f0f0")
        input_frame.pack(pady=10)    
        input_field = tk.Entry(input_frame, font=('Arial', 20), textvariable=self.input_text, width=25, bd=5, relief=tk.RIDGE, justify="right")
        input_field.grid(row=0, column=0, ipady=10)
        btns_frame = tk.Frame(self.root, bg="#f0f0f0")
        btns_frame.pack()
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        
        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                self.create_button(btns_frame, button, row_index, col_index)

    def create_button(self, frame, text, row, col):
        btn = tk.Button(frame, text=text, width=7, height=3, font=('Arial', 14), command=lambda: self.on_button_click(text), bg="white", fg="black", relief=tk.RAISED)
        btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
