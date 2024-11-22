import sqlite3
import login
#from login import *
import newdatabase
import os
import tkinter
from tkinter import *
import tkinter as tk



#3 functions linking the click of the button to funcitons
def login_click():
  login.newUser()
  
#-^
def user_click():
    login.login()

#-^
def exit_click():
  exit()


#creating main gui
root = tk.Tk()
root.title("Main Menu")
root.geometry("1000x800")


# Main Menu Frame
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill="both", expand=True)



#Button functions
login = Button(main_menu_frame, text="Login", command=user_click).pack(pady=10)


newuser = Button(main_menu_frame, text="Create New User", command=login_click).pack(pady=10)



#, command=login.newUser()
#, command=login.login()




root.mainloop()