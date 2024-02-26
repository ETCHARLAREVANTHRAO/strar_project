import tkinter as tk
import math

def f(x):
    return eval(user_input.get())

xmin = -10
xmax = 10

width = 500
height = 500
pixels_per_unit = 50

root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height, bg='white')
canvas.pack()
canvas.create_line(0, height/2, width, height/2, fill='black')
canvas.create_line(width/2, 0, width/2, height, fill='black')

user_input = tk.Entry(root)
user_input.pack()

def update_graph(event):
    canvas.delete('all')
    canvas.create_line(0, height/2, width, height/2, fill='black')
    canvas.create_line(width/2, 0, width/2, height, fill='black')
    for i in range(width):
        x = xmin + (i / pixels_per_unit)
        y = height/2 - (f(x) * pixels_per_unit)
        canvas.create_oval(i, y, i+1, y+1, fill='black')

user_input.bind('<Return>', update_graph)

root.mainloop()

#example ---> math.sin(x)