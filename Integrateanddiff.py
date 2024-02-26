import tkinter as tk
from sympy import Symbol, integrate, diff

root = tk.Tk()
root.title("Integration and Differentiation Calculator")
root.geometry("600x400")

def integrate_function():

    function_input = function_entry.get()
    x = Symbol('x')

    try:
        integrated_function = integrate(function_input, x)
        intermediate_steps_text.delete("1.0", tk.END)
        intermediate_steps_text.insert(tk.END, f"Function: {function_input}\n\n")
        intermediate_steps_text.insert(tk.END, "Intermediate steps:\n\n")
        intermediate_steps_text.insert(tk.END, f"Antiderivative of {function_input}: {integrated_function}\n\n")
        intermediate_steps_text.insert(tk.END, f"Final Result: {integrated_function + ' + C'}\n")

        output_label.config(text="Result: " + str(integrated_function) + " + C")
    except:
        output_label.config(text="Error: Invalid Input")


def differentiate_function():
    function_input = function_entry.get()

    x = Symbol('x')

    try:
        differentiated_function = diff(function_input, x)

        intermediate_steps_text.delete("1.0", tk.END)
        intermediate_steps_text.insert(tk.END, f"Function: {function_input}\n\n")
        intermediate_steps_text.insert(tk.END, "Intermediate steps:\n\n")
        intermediate_steps_text.insert(tk.END, f"Derivative of {function_input}: {differentiated_function}\n\n")
        intermediate_steps_text.insert(tk.END, f"Final Result: {differentiated_function}\n")


        output_label.config(text="Result: " + str(differentiated_function))
    except:

        output_label.config(text="Error: Invalid Input")
function_label = tk.Label(root, text="Enter Function:")
function_label.pack()

function_entry = tk.Entry(root)
function_entry.pack()

integrate_button = tk.Button(root, text="Integrate", command=integrate_function)
integrate_button.pack()

differentiate_button = tk.Button(root, text="Differentiate", command=differentiate_function)
differentiate_button.pack()
output_label = tk.Label(root, text="Result: ")

intermediate_steps_label = tk.Label(root, text="Intermediate Steps:")
intermediate_steps_label.pack()

intermediate_steps_text = tk.Text(root)
intermediate_steps_text.pack()

root.mainloop()



# 2*x**2 + 3*x + 1