import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER
		)''')

conn.execute('''CREATE TABLE cart
		(quantity INTEGER,
		productId INTEGER,
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.close()

