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
window.minsize(160, 240)




# pack is used to show the object in the window    
label = tkinter.Label(window, text = "Sports Circuit App").pack()
# function return choice prints out the radio button choice on click
def ReturnChoice():
    print("Your choice is " + str(seriesChoice.get()) + '\n'); 
# code below instantiates radio buttons and ties variable seriesChoice to each button
seriesChoice = tkinter.IntVar()
tkinter.Radiobutton(window,text="Rally",padx = 20,variable=seriesChoice,value=1,command=ReturnChoice).pack(anchor=tkinter.W)
tkinter.Radiobutton(window,text="Formula 1",padx = 20,variable=seriesChoice,value=2,command=ReturnChoice).pack(anchor=tkinter.W)
series = ["Rally", "Formula 1"]


seriesChoice = input("Please enter the series you wish to view information on: ")


window.mainloop()
