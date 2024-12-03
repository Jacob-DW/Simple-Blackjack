import sqlite3
import tkinter
from tkinter import *
import tkinter as tk
import maingui
from maingui import *



def leaderboard():

  #need to create a new gui window for then login menu
    leaderboard_frame = tk.Toplevel()
    leaderboard_frame.title("Leaderboard")
    leaderboard_frame.geometry("1000x800")

  #makes the gui auto open on full screen
    leaderboard_frame.attributes("-fullscreen", True)


    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT username FROM user ORDER BY currency DESC LIMIT 5')
        #saves all leaderbaord position in seperate variables
        result = cursor.fetchone()  
        result1 = cursor.fetchone()  
        result2 = cursor.fetchone()  
        result3 = cursor.fetchone()  
        result4 = cursor.fetchone()  

    title=tk.Label(leaderboard_frame, text="Leaderboard", font=('Times', 54))
    title.pack()

    resultpos=tk.Label(leaderboard_frame, text="1", font=('Times', 18))
    resultpos.pack(padx=500)

    result=tk.Label(leaderboard_frame, text=result, font=('Times', 18))
    result.pack(pady=15)

    result1=tk.Label(leaderboard_frame, text=result1, font=('Times', 18))
    result1.pack(pady=15)

    result2=tk.Label(leaderboard_frame, text=result2, font=('Times', 18))
    result2.pack(pady=15)

    result3=tk.Label(leaderboard_frame, text=result3, font=('Times', 18))
    result3.pack(pady=15)

    result4=tk.Label(leaderboard_frame, text=result4, font=('Times', 18))
    result4.pack(pady=15)
       