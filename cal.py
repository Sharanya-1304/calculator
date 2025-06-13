import tkinter as tk
from math import *

# Main window
root = tk.Tk()
root.title("Pastel Calculator")
root.geometry("360x500")
root.config(bg="#fce4ec")

# Input field
expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root, bg="#fce4ec")
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 24), bd=10, width=15, relief=tk.RIDGE, justify='right')
input_field.grid(row=0, column=0, ipady=10)

# Button click handler
def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Button styles
button_font = ('Arial', 18)
button_colors = {
    'pink': '#f78fb3',
    'yellow': '#feca57',
    'green': '#1dd1a1',
    'purple': '#a29bfe',
    'blue': '#74b9ff'
}

# Create a button
def create_button(frame, text, color, row, column, colspan=1, command=None):
    btn = tk.Button(frame, text=text, font=button_font, bg=button_colors[color], fg="white",
                    width=5, height=2, bd=0, relief=tk.RAISED, command=command or (lambda: click(text)))
    btn.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5)

# Buttons layout
btns_frame = tk.Frame(root, bg="#fce4ec")
btns_frame.pack()

buttons = [
    [('C', 'pink', clear), ('%', 'yellow', None), ('/', 'purple', None), ('*', 'purple', None)],
    [('7', 'yellow', None), ('8', 'yellow', None), ('9', 'yellow', None), ('-', 'purple', None)],
    [('4', 'green', None), ('5', 'green', None), ('6', 'green', None), ('+', 'purple', None)],
    [('1', 'pink', None), ('2', 'pink', None), ('3', 'pink', None), ('=', 'blue', evaluate)],
    [('0', 'blue', None), ('.', 'blue', None)]
]

for r, row in enumerate(buttons):
    for c, (txt, clr, cmd) in enumerate(row):
        colspan = 2 if txt == '0' else 1
        create_button(btns_frame, txt, clr, r, c if txt != '0' else 0, colspan=colspan, command=cmd)

root.mainloop()