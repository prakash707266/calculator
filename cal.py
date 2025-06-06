import tkinter as tk
import math

def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    input_text.set(result)
    expression = ""

def scientific_func(func):
    global expression
    try:
        value = float(expression)
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        else:
            result = "Err"
        input_text.set(str(result))
        expression = str(result)
    except:
        input_text.set("Error")
        expression = ""

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
expression = ""
input_text = tk.StringVar()

entry = tk.Entry(root, textvar=input_text, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ['7', '8', '9', '/', 'sin'],
    ['4', '5', '6', '*', 'cos'],
    ['1', '2', '3', '-', 'tan'],
    ['0', '.', '=', '+', 'log'],
    ['C', 'sqrt']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn_text = buttons[i][j]
        btn = tk.Button(root, text=btn_text, font="Arial 18", padx=15, pady=15)
        btn.grid(row=i+1, column=j)

        if btn_text == "=":
            btn.config(command=equal)
        elif btn_text == "C":
            btn.config(command=clear)
        elif btn_text in ["sin", "cos", "tan", "log", "sqrt"]:
            btn.config(command=lambda bt=btn_text: scientific_func(bt))
        else:
            btn.bind("<Button-1>", click)

root.mainloop()