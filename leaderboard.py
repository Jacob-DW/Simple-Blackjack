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
        cursor.execute('SELECT username, currency FROM user ORDER BY currency DESC LIMIT 5')
        #saves all leaderbaord position in seperate variables
        results=[]
        for i in range (0, 5):          
          result = cursor.fetchone()
          results.append(result)  
  

        
    title=tk.Label(leaderboard_frame, text="Leaderboard", font=('Times', 84))
    title.pack()
    
    position=["1.     ","2.     ","3.     ","4.     ","5.     "]

    for j in range (0, 5):
        #create a new fram e for each row so it can be placed side by side
      row_frame = tk.Frame(leaderboard_frame)
      row_frame.pack(pady=15)
      
      resultpos=tk.Label(row_frame, text=position[j], font=('Times', 18))
      resultpos.pack(side="left")

      result=tk.Label(row_frame, text=results[j], font=('Times', 18))
      result.pack(pady=15)


