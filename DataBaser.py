import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Email TEXT NOT NULL,
    Birth TEXT NOT NULL,
    Username TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Connected!")