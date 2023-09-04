import sqlite3


db = sqlite3.connect("Day-63/db_trial/books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")