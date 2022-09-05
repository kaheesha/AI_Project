from distutils.cmd import Command
import sys
import os
from tkinter import *

top = Tk()
top.geometry('550x200')

def OpenCamera():
    os.system('python code.py')

def ReadFile():
    os.system('python readFile.py')

B= Button(top, text="Open Camera", command= OpenCamera)
B1= Button(top, text="Open Attendance", command= ReadFile)
B.pack()
B1.pack()
top.mainloop()