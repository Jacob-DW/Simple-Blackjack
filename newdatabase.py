import sqlite3
import os

# Open connection
db_path = r"C://Users//VMUser2//Documents//python//database.db"
print("Using database file:", os.path.abspath(db_path))  # Print the absolute path

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Print existing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Existing tables:", tables)

# Print table structure (if 'user' exists)
cursor.execute("PRAGMA table_info('user');")
columns = cursor.fetchall()
print("Table columns:", columns)




with sqlite3.connect("database.db") as db:
  cursor = db.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    currency REAL NOT NULL DEFAULT 100.0
  );
  ''')

