from tkinter import *
from subprocess import *


def matrix():
    proc = Popen("gui_matrix.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

def graph_ex():
    proc = Popen("graph_expre.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

def evalution():
    proc = Popen("expres_eval.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

def inte_deff():
    proc = Popen("Integrateanddiff.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

if __name__ == '__main__':
    Master = Tk()
    frame = Frame(Master)
    frame.pack()
    Button(frame, text="Matrix",bd= 4,padx=20,activeforeground="blue", command=matrix).grid(row=0, column=0, padx= 20, pady=8)
    Button(frame, text="Graph", bd= 4, padx=20,activebackground="blue", command=graph_ex).grid(row=0, column=1, padx=20, pady=8)
    Button(frame, text= "Integration and differentiation", bd= 4, padx=20, activeforeground="blue",command=inte_deff).grid(row=0, column=2, padx=20, pady=8)
    Button(frame, text="Expression evalution", bd =4, padx=20, activeforeground="blue", command=evalution).grid(row=0, column=3, padx=20, pady=8)

    output = Text(Master, width=100, height=20)

    output.pack()
    Master.mainloop()
