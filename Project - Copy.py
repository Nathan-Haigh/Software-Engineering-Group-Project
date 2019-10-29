#Project for Software Engineering 
#Timothy Richards, Edward Pidd, Chloe Dooley, Nathan Haigh
#Date Started 29/10/2019

import tkinter

from tkinter import *
from tkinter.ttk import *
from time import strftime

window = tkinter.Tk()
# function used to create window and then rename

window.title("GUI")

# pack is used to show the object in the window

label = tkinter.Label(window, text = "Sports Circuit App").pack()
window.mainloop()

window.minsize(160, 240)

series = ["Rally", "Formula 1"]

seriesChoice = input("Please enter the series you wish to vie information on: ")
print("Your choice is" + seriesChoice)
