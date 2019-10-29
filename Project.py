#Project for Software Engineering 
#Timothy Richards, Edward Pidd, Chloe Dooley, Nathan Haigh
#Date Started 29/10/2019

# Imports
import tkinter
import datetime

from tkinter import *
from tkinter.ttk import *
from time import strftime
# Instantiate window
window = tkinter.Tk()

# Function used to create window and then rename
window.title("GUI")
window.minsize(300, 400)

# Pack is used to show the object in the window    
label = tkinter.Label(window, text = "Sports Circuit App").pack()

# Function ReturnChoice() prints out the radio button choice when it is clicked -- series[seriesChoice.get()] will get the relevant radio button choice from the array
def ReturnChoice():
    print("Your choice is " + series[seriesChoice.get()] + '\n' ); 
    if(series[seriesChoice.get()] == series[1]):
        print (f1Racesinfo[0][0] +" on the " + f1Racesinfo [1][0]) 
    
# Code below instantiates radio buttons and ties variable seriesChoice to each button
seriesChoice = tkinter.IntVar()
tkinter.Radiobutton(window,text="Rally",padx = 20,variable=seriesChoice,value=0,command=ReturnChoice).pack(anchor=tkinter.W)
tkinter.Radiobutton(window,text="Formula 1",padx = 20,variable=seriesChoice,value=1,command=ReturnChoice).pack(anchor=tkinter.W)


# Define series data array
series = ["Rally", "Formula 1"]
f1Racesinfo=[["Circuit of the Americas","Autódromo José Carlos Pace"],["2019,11,3","2019,11,17"]]



    


# This generates the window - keep at bottom of code
window.mainloop()