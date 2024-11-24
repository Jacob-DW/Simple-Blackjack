import sqlite3
import login
#from login import *
import newdatabase
import os
import tkinter
from tkinter import *
import tkinter as tk
import maingui
from maingui import *


#3 functions linking the click of the button to funcitons
def login_click():
  login.newUser()
  
#-^
def user_click():
  login.login()

#-^
def exit_click():
  exit()



# Main Menu Frame
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill="both", expand=True)


#Title on menu screen
title=tk.Label(main_menu_frame, text="Card Game", width=15, height=15, font=('Times', 54))
title.place(x=300, y=0)

#login button on menu screen
login_button = Button(main_menu_frame, text="Login", command=user_click, width=20, height=10, font=('Times', 14))
login_button.place(x=100, y=100)
#special animations when the buttons are hovered over
login_button.config(cursor="hand2")
login_button.bind("<Enter>", lambda e: login_button.config(bg="grey"))
login_button.bind("<Leave>", lambda e: login_button.config(bg="white"))


#create new user button on menu screen
newuser_button = Button(main_menu_frame, text="Create New User", command=login_click, width=20, height=10, font=('Times', 14))
newuser_button.place(x=100, y=400)
#special animations when the buttons are hovered over
newuser_button.config(cursor="hand2")
newuser_button.bind("<Enter>", lambda e: newuser_button.config(bg="grey"))
newuser_button.bind("<Leave>", lambda e: newuser_button.config(bg="white"))

#create games button on menu screen
games_button=tk.Button(main_menu_frame, text="Games", width=20, height=10,font=('Times', 14))
games_button.config(text="Games", state="disabled", bg="gray")
games_button.place(x=900, y=100)

#create tutorial button on menu screen
tutorial_button=tk.Button(main_menu_frame, text="Tutorial", width=20, height=10,font=('Times', 14))
tutorial_button.place(x=100, y=700)
#special animations when the buttons are hovered over
tutorial_button.config(cursor="hand2")
tutorial_button.bind("<Enter>", lambda e: tutorial_button.config(bg="grey"))
tutorial_button.bind("<Leave>", lambda e: tutorial_button.config(bg="white"))

#create leaderbaord button on menu screen
leaderboard_button=tk.Button(main_menu_frame, text="Leaderboard", width=20, height=10,font=('Times', 14))
leaderboard_button.place(x=900, y=400)
#special animations when the buttons are hovered over
leaderboard_button.config(cursor="hand2")
leaderboard_button.bind("<Enter>", lambda e: leaderboard_button.config(bg="grey"))
leaderboard_button.bind("<Leave>", lambda e: leaderboard_button.config(bg="white"))

#create settings button on menu screen
settings_button=tk.Button(main_menu_frame, text="Settings", width=20, height=10,font=('Times', 14))
settings_button.place(x=900, y=700)
#special animations when the buttons are hovered over
settings_button.config(cursor="hand2")
settings_button.bind("<Enter>", lambda e: settings_button.config(bg="grey"))
settings_button.bind("<Leave>", lambda e: settings_button.config(bg="white"))

root.mainloop()