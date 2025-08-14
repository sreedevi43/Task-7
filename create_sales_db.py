# Import the built-in SQLite library to work with .db files
import sqlite3

# Open a connection to (or create) a database file named "sales_data.db"
conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

#  Created a table named `sales` if it doesn't already exist
# - id: auto-incrementing primary key
# - date: text column for the sale date (ISO format recommended: YYYY-MM-DD)
# - product: text column for the product name
# - quantity: integer column for units sold
# - price: real (float) column for unit price
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TEXT NOT NULL,
  product TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  price REAL NOT NULL
);
""")

# Prepared multiple rows of sample data as a list of tuples
# Each tuple matches the columns (date, product, quantity, price)
rows = [
  ("2025-07-01","Laptop",2,750.00),
  ("2025-07-01","Phone",3,400.00),
  ("2025-07-02","Headphones",5,60.00),
]

# Inserted all rows in one call using a parameterized query (avoids SQL injection)
cur.executemany("INSERT INTO sales(date,product,quantity,price) VALUES (?,?,?,?)", rows)

# To Permanently save (commit) the changes to the database file
conn.commit()
conn.close()
