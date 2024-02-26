from tkinter import *
from subprocess import *

def read_file():
    proc = Popen("InfoProvider.py", stdout=PIPE, shell= True)
    proc = proc.communicate()
    output.insert(END, proc)


if __name__ == '__main__':
    Master = Tk()
    frame = Frame(Master)
    output = Text(Master, width=100, height=20)
    read_file()
    output.pack()
    Master.mainloop()
