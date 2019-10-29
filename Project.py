#Project for Software Engineering 
#Timothy Richards, Edward Pidd, Chloe Dooley, Nathan Haigh
#Date Started 29/10/2019

# Imports
import tkinter

from tkinter import *
from tkinter.ttk import *
from time import strftime
# Instantiate window
window = tkinter.Tk()

# Function used to create window and then rename
window.title("GUI")
window.minsize(160, 240)

# Pack is used to show the object in the window    
label = tkinter.Label(window, text = "Sports Circuit App").pack()

# Function ReturnChoice() prints out the radio button choice when it is clicked -- series[seriesChoice.get()] will get the relevant radio button choice from the array
def ReturnChoice():
    print("Your choice is " + series[seriesChoice.get()] + '\n' ); 
    
# Code below instantiates radio buttons and ties variable seriesChoice to each button
seriesChoice = tkinter.IntVar()
tkinter.Radiobutton(window,text="Rally",padx = 20,variable=seriesChoice,value=0,command=ReturnChoice).pack(anchor=tkinter.W)
tkinter.Radiobutton(window,text="Formula 1",padx = 20,variable=seriesChoice,value=1,command=ReturnChoice).pack(anchor=tkinter.W)

# Define series data array
series = ["Rally", "Formula 1"]










# This generates the window - keep at bottom of code
window.mainloop()