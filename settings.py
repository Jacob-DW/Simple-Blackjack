import sqlite3
import time
import tkinter
from tkinter import *
import tkinter as tk
#import maingui
#from maingui import *


def settings():
    settings_frame = tk.Toplevel()
    settings_frame.title("Settings")
    settings_frame.geometry("1000x800")

    #makes the gui auto open on full screen
    settings_frame.attributes("-fullscreen", True)

    #on/off button on menu screen
    cb_on_button = Button(settings_frame, text="On", width=20, height=10, font=('Times', 14), bg="white")
    cb_on_button.place(x=100, y=100)
    #special animations when the buttons are hovered over
    cb_on_button.config(cursor="hand2")
    cb_on_button.bind("<Enter>", lambda e: cb_on_button.config(bg="grey"))
    cb_on_button.bind("<Leave>", lambda e: cb_on_button.config(bg="white"))

    cb_off_button = Button(settings_frame, text="Off", width=20, height=10, font=('Times', 14), bg="white")
    cb_off_button.place(x=500, y=100)
    #special animations when the buttons are hovered over
    cb_off_button.config(cursor="hand2")
    cb_off_button.bind("<Enter>", lambda e: cb_off_button.config(bg="grey"))
    cb_off_button.bind("<Leave>", lambda e: cb_off_button.config(bg="white"))