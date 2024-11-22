import sqlite3
import time


def login():
  while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with sqlite3.connect("database.db") as db:
      cursor = db.cursor()
    find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
    cursor.execute(find_user,[(username),(password)])
    results = cursor.fetchall()

    if results:
      for i in results:
        print("Welcome ",i[2])
        return(i[0])
    else:
      print("Username and password not recognised")
      again = input("Do you want to retry (Y/N) ")
      if again.lower() == "n":
        print("Goodbye")
        time.sleep(1)
        return("exit")


def newUser():
  print("Add new user")
  found = 0
  while found == 0:
    username = input("Enter a username: ")
    with sqlite3.connect("database.db") as db:
      cursor = db.cursor()
    find_user = ('SELECT * FROM user WHERE username = ?')
    cursor.execute(find_user,[(username)])

    if cursor.fetchall():
      print("username taken")
    else:
      found=1

    firstname = input("Please enter you firstname: ")
    surname = input("Please enter you surname: ")
    password = input("Please enter you password: ")
    password1 = input("Please enter you password again: ")
    while password != password1:
      print("Passwords did not match")
      password=input("Please enter you password: ")
      password1=input("Please enter you password again: ")

    insertData = '''INSERT INTO user(username,firstname,surname,password) VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username), (firstname), (surname), (password)])