#Project for Software Engineering 
#Timothy Richards, Edward Pidd, Chloe Dooley, Nathan Haigh
#Date Started 29/10/2019

# Imports
import tkinter
import datetime
import tweepy

from tkinter import *
from tkinter.ttk import *
from time import strftime
# Instantiate window
window = tkinter.Tk()

# Function used to create window and then rename
window.title("GUI")
window.minsize(600, 800)

# Pack is used to show the object in the window    
label = tkinter.Label(window, text = "Sports Circuit App").pack()

# Define series data array
series = ["Rally", "Formula 1"]
f1Race=["Australian Grand Prix","Bahrain Grand Prix","Vietnamese Grand Prix","Chinese Grand Prix","Dutch Grand Prix","Spanish Grand Prix","Monaco Grand Prix","Azerbaijani Grand Prix","Canadian Grand Prix","French Grand Prix","Austrian Grand Prix","British Grand Prix","Hungarian Grand Prix","Belgian Grand Prix","Italian Grand Prix","Singapore Grand Prix","Russian Grand Prix","Japanese Grand Prix","United States Grand Prix","Mexican Grand Prix","Brazilian Grand Prix","Abu Dhabi Grand Prix"]
f1Date=["Mar 13-15","Mar 20-22","Apr 3-5","Apr 17-19","May 1-3","May 8-10" ,"May 21-24", "Jun 5-7" ,"Jun 12-14" ,"Jun 26-28" ,"Jul 3-5" ,"Jul 17-19" ,"Jul 31-Aug 2", " Aug 28-30" ,"Sep 4-6", "Sep 18-20" ,"Sep 25-27" ,"Oct 9-11" ,"Oct 23-25" ," Oct 30-Nov 1" ,"Nov 13-15" ,"Nov 27-29"]
f1Circuit=["Albert Park","Bahrain International Circuit","Hanoi","Shanghai International Circuit","Zandvoort","Circuit de Catalunya","Monaco","Baku City Circuit","Circuit Gilles Villeneuve","Paul Ricard","Red Bull Ring","Silverstone","Hungaroring","Spa-Francorchamps","Monza","Singapore","Sochi Autodrom","Suzuka","Circuit of the Americas","Autodromo Hermanos Rodriguez","Interlagos","Yas Marina"]
place = 0

# twitter passwords 
auth = tweepy.OAuthHandler("xTw4DTrjDfEmcNC62bHz8QSPn" , "zbk8hD0xV3M7r9sZYEawmZx8FbkLo4zBRQEYPanW8K3qbdzWKv" )
auth.set_access_token("3233925630-aLsF2vD1j6FdBaV4HG1iHLeeJpjHB46A0DkVAC6" , "1ySAsPgGJ0ch22OID0k7Cj5qYD8MCAce2ITeshT0Q9MVR" )




# Function ReturnChoice() prints out the radio button choice when it is clicked -- series[seriesChoice.get()] will get the relevant radio button choice from the array
def ReturnChoice():
    print("Your choice is " + series[seriesChoice.get()] + '\n' ); 
    if(series[seriesChoice.get()] == series[1]):
        #print (f1Racesinfo[0][0] +" on the " + f1Racesinfo [1][0]) 
        text.delete('1.0', END)
        text.insert(tkinter.END,f1Race[place] +"\nStarting the " + f1Date [place] + " 2020" + "\nLocation " + f1Circuit[place] + "\nWeather" )
    else:
        text.delete('1.0', END)
        text.insert(tkinter.END," Next Rally")

def add1():
    global place
    print (place)
    if(place >=21):
        place = 0
        ReturnChoice()
    else: 
        place = place + 1
        ReturnChoice()
        print (place)

def take1():
    global place
    print(place)
    if (place >= 0): 
        place = place - 1
        ReturnChoice()
    else:
        place = 21
        ReturnChoice()
    
# Code below instantiates radio buttons and ties variable seriesChoice to each button
seriesChoice = tkinter.IntVar()
tkinter.Radiobutton(window,text="Formula 1",padx = 20,variable=seriesChoice,value=1,command=ReturnChoice).pack(anchor=tkinter.W)
tkinter.Radiobutton(window,text="Rally",padx = 20,variable=seriesChoice,value=0,command=ReturnChoice).pack(anchor=tkinter.W)


text = Text(window, width=40, height=10)
text.pack()


next = tkinter.Button(window, text="Next", command =lambda: add1())
next.pack()

last = Button(window, text="Last", command = lambda:take1())
last.pack()

twitter = Text(window,width=40,height=10)
twitter.pack()

api = tweepy.API(auth)
tweets=api.user_timeline(screen_name = 'F1',count=10)
for tweet in tweets:
     if "#BrazilGP" in tweet.text:
         lasttweet=tweet.text
         twitter.insert(tkinder.END,"tedt")
         print(lasttweet)

# This generates the window - keep at bottom of code
window.mainloop()
