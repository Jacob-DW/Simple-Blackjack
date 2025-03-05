import sqlite3
import time
import tkinter
from tkinter import *
import tkinter as tk
import maingui
from maingui import *
import blackjack


def blackjack_click():
  blackjack.cards()






def login():

  #binds the escape button to close the window
  def login_exit_click(event=None):
    login_frame = event.widget
    try:
      login_frame.destroy()
    except tk.TclError:
      pass
    
  root.bind('<Escape>', login_exit_click)

  #need to create a new gui window for then login menu
  login_frame = tk.Toplevel()
  login_frame.title("Login")
  login_frame.geometry("1000x800")

  #makes the gui auto open on full screen
  login_frame.attributes("-fullscreen", True)

  newusertext=tk.Label(login_frame, text="Login to your account", font=('Times', 24))
  newusertext.pack(pady=5)

  
  #username
  usernametext=tk.Label(login_frame, text="Enter username", font=('Times', 18))
  usernametext.pack(pady=15)
    
  usernametextbox=tk.Entry(login_frame)
  usernametextbox.pack(pady=5)

  #password
  passwordtext=tk.Label(login_frame, text="Enter password",font=('Times', 18))
  passwordtext.pack(pady=5)
    
  passwordtextbox=tk.Entry(login_frame, show = '*')
  passwordtextbox.pack(pady=5)
   
  def textboxvalue():
    login_button.config(state=tk.DISABLED)
    login_button.after(3000, lambda: login_button.config(state=tk.NORMAL))
    username = usernametextbox.get()
    password = passwordtextbox.get()

    with sqlite3.connect("database.db") as db:
      cursor = db.cursor()
    find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
    cursor.execute(find_user,[(username),(password)])
    results = cursor.fetchall()



    if not username or not password:
      fieldserror=tk.Label(login_frame, text="All fields are requried to login", font=('Times', 18))
      fieldserror.pack(pady=5)
      login_frame.after(2000, fieldserror.destroy)
      

    else:

      if results:
        correctlogin=tk.Label(login_frame, text="Welcome, you have a currency of:", font=('Times', 18))
        correctlogin.pack(pady=5)
        #NEEDS TO BE CHANGED TO 3000 ISH ONCE TESTING IS DONE
        login_frame.after(1000, lambda : login_frame.destroy())

        #create new enables instance of games button once user logs in
        games_button1=tk.Button(root, text="Games", command=blackjack_click ,width=20, height=10,font=('Times', 14), bg="white")
        games_button1.config(text="Games", bg="White")
        games_button1.place(x=800, y=100) #x=1600 once off lapotp
        games_button1.config(cursor="hand2")
        games_button1.bind("<Enter>", lambda e: games_button1.config(bg="grey"))
        games_button1.bind("<Leave>", lambda e: games_button1.config(bg="white"))
        

        #function to find out how much currency user has and displays
      with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT currency FROM user WHERE username = ?', (username,))
        result = cursor.fetchall()  
        if result:
            currency = result[0] 
            currencylabel=tk.Label(login_frame, text=currency,font=('Times', 18))
            currencylabel.pack(pady=5)

        else:
          incorrectlogin=tk.Label(login_frame, text="Username and password not recognised", font=('Times', 18))
          incorrectlogin.pack(pady=5)
          login_frame.after(2000, incorrectlogin.destroy)

  login_button=tk.Button(login_frame, text="Login", command=textboxvalue)
  login_button.pack(pady=20)
  #special animations when the buttons are hovered over
  login_button.config(cursor="hand2")
  login_button.bind("<Enter>", lambda e: login_button.config(bg="grey"))
  login_button.bind("<Leave>", lambda e: login_button.config(bg="white"))
 






def newUser():

  def textboxvalue():
    username = usernametextbox.get()
    firstname = fistnametextbox.get()
    surname = surnametextbox.get()
    password = passwordtextbox.get()
    password1 = password1textbox.get()

    save_button.config(state=tk.DISABLED)
    save_button.after(3000, lambda: save_button.config(state=tk.NORMAL))

    with sqlite3.connect("database.db") as db:
      cursor = db.cursor()
    find_user = ('SELECT * FROM user WHERE username = ?')
    cursor.execute(find_user,[(username)])

    if cursor.fetchall():
      usernametaken=tk.Label(newuser_frame, text="Username taken", font=('Times', 18))
      usernametaken.pack(pady=5)
      newuser_frame.after(2000, usernametaken.destroy)
      return

    if password != password1:
      passworderror=tk.Label(newuser_frame, text="Passwords dont match", font=('Times', 18))
      passworderror.pack(pady=5)
      newuser_frame.after(2000, passworderror.destroy)
      return
    
    if not username or not firstname or not surname or not password or not password1:
      fieldserror=tk.Label(newuser_frame, text="All fields are requried to save", font=('Times', 18))
      fieldserror.pack(pady=5)
      newuser_frame.after(2000, fieldserror.destroy)

    else:
      insertData = '''INSERT INTO user(username,firstname,surname,password) VALUES(?,?,?,?)'''
      cursor.execute(insertData,[(username), (firstname), (surname), (password)])
      db.commit()
      accountcreated=tk.Label(newuser_frame, text="Account Created", font=('Times', 18))
      accountcreated.pack(pady=5)
      newuser_frame.after(3000, lambda : newuser_frame.destroy())




  #binds the escape button to close the window
  def newuser_exit_click(event=None):
    newuser_frame = event.widget
    try:
      newuser_frame.destroy()
    except tk.TclError:
      pass

  root.bind('<Escape>', newuser_exit_click)

  #need to create a new gui window for then new user menu
  newuser_frame = tk.Toplevel()
  newuser_frame.title("New User")
  newuser_frame.geometry("3000x1800")


 #makes the gui auto open on full screen
  newuser_frame.attributes("-fullscreen", True)

  newusertext=tk.Label(newuser_frame, text="Add new user", font=('Times', 24))
  newusertext.pack(pady=5)

  #username
  usernametext=tk.Label(newuser_frame, text="Enter username", font=('Times', 18))
  usernametext.pack(pady=5)
    
  usernametextbox=tk.Entry(newuser_frame)
  usernametextbox.pack(pady=5)

#firstname
  firstnametext=tk.Label(newuser_frame, text="Enter firstname", font=('Times', 18))
  firstnametext.pack(pady=5)
    
  fistnametextbox=tk.Entry(newuser_frame)
  fistnametextbox.pack(pady=5)

#surname
  surnametext=tk.Label(newuser_frame, text="Enter surname", font=('Times', 18))
  surnametext.pack(pady=5)
    
  surnametextbox=tk.Entry(newuser_frame)
  surnametextbox.pack(pady=5)

#password
  passwordtext=tk.Label(newuser_frame, text="Enter password", font=('Times', 18))
  passwordtext.pack(pady=5)
    
  passwordtextbox=tk.Entry(newuser_frame, show = "*")
  passwordtextbox.pack(pady=5)

#password again
  password1text=tk.Label(newuser_frame, text="Enter password again", font=('Times', 18))
  password1text.pack(pady=5)
    
  password1textbox=tk.Entry(newuser_frame, show = "*")
  password1textbox.pack(pady=5)


  save_button=tk.Button(newuser_frame, text="Save", command=textboxvalue, bg="white")
  save_button.pack(pady=30)
  #special animations when the buttons are hovered over
  save_button.config(cursor="hand2")
  save_button.bind("<Enter>", lambda e: save_button.config(bg="grey"))
  save_button.bind("<Leave>", lambda e: save_button.config(bg="white"))



