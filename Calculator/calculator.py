import tkinter as tk

def button_click(value):
    current = textbox.get("1.0", tk.END).strip()  
    textbox.config(state=tk.NORMAL)  
    textbox.delete("1.0", tk.END)  
    textbox.insert("1.0", current + value)  
    textbox.config(state=tk.DISABLED) 

def calculate_result():
    try:
        expression = textbox.get("1.0", tk.END).strip()  
        result = eval(expression)  
        textbox.config(state=tk.NORMAL)  
        textbox.delete("1.0", tk.END) 
        textbox.insert("1.0", str(result))  
        textbox.config(state=tk.DISABLED)  
    except Exception as e:
        textbox.config(state=tk.NORMAL)  
        textbox.delete("1.0", tk.END)  
        textbox.insert("1.0", "Error") 
        textbox.config(state=tk.DISABLED)  

def clear_text():
    textbox.config(state=tk.NORMAL) 
    textbox.delete("1.0", tk.END)  
    textbox.config(state=tk.DISABLED) 

root = tk.Tk()
root.geometry("400x350")
root.configure(bg='White')

root.title("Calculator")

textbox = tk.Text(root, height=3, font=('Arial', 16), state=tk.DISABLED, bg="white",relief="ridge", borderwidth=2)
textbox.pack(pady=20,padx=20)

buttonframe = tk.Frame(root, relief="ridge", borderwidth=2)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('C', 3, 1), ('/', 3, 2), ('=', 3, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(buttonframe, text=text, font=('Arial', 18), bg="gray99", fg="orange red", 
                        command=calculate_result, borderwidth=0, relief="flat", padx=2, pady=2)
    elif text == "C":
        btn = tk.Button(buttonframe, text=text, font=('Arial', 18), bg="gray99", fg="orange red",
                        command=clear_text, borderwidth=0, relief="flat", padx=2, pady=2)
    else:
        btn = tk.Button(buttonframe, text=text, font=('Arial', 18), fg="black", bg="gray99", 
                        command=lambda t=text: button_click(t), borderwidth=0, relief="flat", padx=2, pady=2)
    
    btn.grid(row=row, column=col, sticky=tk.W + tk.E)

buttonframe.pack(fill='x', padx=20)

root.mainloop()

