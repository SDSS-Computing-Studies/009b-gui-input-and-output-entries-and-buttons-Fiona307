"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
#!python3

import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Madlib Invitation")

def proceed():
    name = e4.get()
    adverb = e5.get()
    noun = e6.get()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e1.insert(0,name)
    e2.insert(0,adverb)
    e3.insert(0,noun)

output1 = StringVar()
output2 = StringVar()
output3 = StringVar()
output4 = StringVar()
output5 = StringVar()
output6 = StringVar()

output1.set("(Enter a name in the box below)")
output2.set("(Enter an adverb in the box below)")
output3.set("(Enter a noun in the box below)")

e4 = tk.Entry(win, textvariable=output4)
e5 = tk.Entry(win, textvariable=output5)
e6 = tk.Entry(win, textvariable=output6)

l4 = tk.Label(win, text="Dear ")
l5 = tk.Label(win, text=",")
l6 = tk.Label(win, text="You are ")
l7 = tk.Label(win, text="invited!")
l8 = tk.Label(win, text="It's time for a ")
l9 = tk.Label(win, text="!")

e1 = tk.Entry(win, width=30, textvariable=output1)
e2 = tk.Entry(win, width=30, textvariable=output2)
e3 = tk.Entry(win, width=30, textvariable=output3)

b1 = tk.Button(win, text="proceed", command=proceed)

l4.grid(row=1, column=1)
e1.grid(row=1, column=2)
l5.grid(row=1, column=3)
e4.grid(row=2, column=2)
l6.grid(row=3, column=1)
e2.grid(row=3, column=2)
e5.grid(row=4, column=2)
l7.grid(row=3, column=3)
l8.grid(row=6, column=1)
e3.grid(row=6, column=2)
l9.grid(row=6, column=3)
e6.grid(row=7, column=2)
b1.grid(row=8, column=3)

win.mainloop()