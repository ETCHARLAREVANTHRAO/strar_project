import os
import sys
import cv2
from tkinter import *
from subprocess import *
from PIL import ImageTk, Image

def caluculator():
    proc = Popen("AdvCalculator.py", stdout=PIPE, shell=True)
    proc.communicate()

def scheduler():
    proc = Popen("Scheduler.py", stdout=PIPE, shell=True)
    proc.communicate()

def infoprovider():
    proc = Popen("info.py", stdout=PIPE, shell=True)
    proc.communicate()

def predictor():
    proc = Popen("Predector.py", stdout=PIPE, shell= True)
    proc.communicate()

def basicTools():
    proc = Popen("VolumeHandControl.py", stdout=PIPE, shell=True)
    proc.communicate()

def stop():
    sys.exit()
if __name__ == '__main__':
    Master = Tk()

    frame = Frame(Master)
    frame.pack()

    img_info = Image.open("images/icons8-bookmark-50.png").resize((40,30))
    photo = ImageTk.PhotoImage(img_info)
    img_predict = Image.open("images/icons8-combo-chart-48.png").resize((40, 30))
    photo1 = ImageTk.PhotoImage(img_predict)
    img_calci = Image.open("images/calculator.png").resize((40, 30))
    photo2 = ImageTk.PhotoImage(img_calci)
    img_sched = Image.open("images/icons8-to-do-50.png").resize((40, 30))
    photo3 = ImageTk.PhotoImage(img_sched)
    img_control = Image.open("images/icons8-compact-camera-50.png").resize((40, 30))
    photo4 = ImageTk.PhotoImage(img_control)
    img_exit = Image.open("images/icons8-cross-mark-48.png").resize((40, 30))
    photo5 = ImageTk.PhotoImage(img_exit)


    label1 = Label(frame, image=photo).grid(row=2, column=0)
    label2 = Label(frame, image=photo1).grid(row=0, column=1)
    label3 = Label(frame, image=photo2).grid(row=0, column=0)
    label4 = Label(frame, image=photo3).grid(row=2, column=1)
    label5 = Label(frame, image=photo4).grid(row=4, column=0)
    label6 = Label(frame, image=photo5).grid(row=4, column=1)

    Button(frame, text="Adv. Calci", bd=4, padx=20, activeforeground="green", command=caluculator).grid(row=1, column=0, padx=20, pady=10)

    Button(frame, text="Predictor", bd=4, padx=20, activeforeground="green", command=predictor).grid(row=1, column=1, padx=20, pady=10)
    Button(frame, text="Info Provider", bd=4, padx=20, activeforeground="green", command=infoprovider).grid(row=3, column=0,padx=20, pady=10)
    Button(frame, text="Scheduler", bd=4, padx=20, activeforeground="green", command=scheduler).grid(row=3, column=1, padx=20, pady=10)
    Button(frame, text="Controls", bd=4, padx=20, activeforeground="green", command=basicTools).grid(row=5, column=0, padx=20, pady=10)
    Button(frame, text="Exit", bd=4, padx=20, activeforeground="green", command=stop).grid(row=5, column=1, padx=20, pady=10)

    #output = Text(Master, width=100, height=20)
    #output.pack()

    Master.mainloop()

