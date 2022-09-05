#CODE TAKEN FROM
# https://stackoverflow.com/questions/62368957/how-to-display-a-csv-file-in-gui-in-tkinter-python

import csv
from tkinter import *
from tkinter import ttk
import tkinter

root = tkinter.Tk()
root.title("Attendance Sheet")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (0.99 * w, 0.9 * h))


def displayontowindow():
    frame = Frame(root, width=600, height=310, bg="light grey")

    frame = ttk.Frame(root, width=300, height=250)

    # Canvas creation with double scrollbar
    hscrollbar = ttk.Scrollbar(frame, orient=tkinter.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame, orient=tkinter.VERTICAL)
    sizegrip = ttk.Sizegrip(frame)
    canvas = tkinter.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set,
                            xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)

    # Add controls here
    subframe = ttk.Frame(canvas)

    # open file
    with open("Attendance.csv", newline="") as file:
        reader = csv.reader(file)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                label = tkinter.Label(subframe, width=10, height=2,
                                      text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    # Packing everything
    subframe.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)
    hscrollbar.pack(fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)
    vscrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
    sizegrip.pack(in_=hscrollbar, side=BOTTOM, anchor="se")
    canvas.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=tkinter.TRUE)
    frame.pack(padx=5, pady=5, expand=True, fill=tkinter.BOTH)

    canvas.create_window(0, 0, window=subframe)
    root.update_idletasks()  # update geometry
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

displayontowindow()

root.mainloop()