import sqlite3

with sqlite3.connect("database.db") as db:
  cursor = db.cursor()


  cursor.execute('''
  CREATE TABLE IF NOT EXISTS user(
  userID INTEGER PRIMARY KEY,
  username VARCHAR(20) NOT NULL,
  firstname VARCHAR(20) NOT NULL,
  surname VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL);
  ''')
