import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    expression = expression_entry.get()
    try:
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# create tkinter window
window = tk.Tk()
window.title("Expression Evaluator")

# create expression input box
expression_label = tk.Label(window, text="Enter expression:")
expression_label.pack()
expression_entry = tk.Entry(window, width=50)
expression_entry.pack()

# create evaluate button
evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_expression)
evaluate_button.pack()

# create result label
result_label = tk.Label(window, text="")
result_label.pack()

# start tkinter event loop
window.mainloop()
