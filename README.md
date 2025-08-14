🛒 Sales Data Setup – SQLite + Python
==========================================

This project is a small starter exercise for working with databases in Python.
It creates a sales database with just a few entries so you can later run SQL queries and make charts.
Think of it as planting seeds before doing the real data analysis.

📋 What This Script Does — Step by Step
========================================

Connects to a database

If sales_data.db doesn’t exist, Python will create it.

If it already exists, we just open it for use.

Sets up a table called sales

Columns:
=========

id → auto-incremented for each sale

date → when the sale happened (YYYY-MM-DD)

product → what was sold

quantity → how many units

price → cost per unit

Adds sample data

Three small sales entries:
========================

2 Laptops at ₹750 each

3 Phones at ₹400 each

5 Headphones at ₹60 each

Saves the changes (commit)

Without committing, the inserted data would disappear after closing.

Closes the connection

Always a good habit — it frees up system resources.

🛠 Tools Used
============

Python 3

SQLite3 (built-in with Python — no extra install needed)

Pandas (for data analysis)

Matplotlib (for chart visualization)

📂 File Overview
==================

create_sales_db.py → Creates the database and inserts the data.

sales_data.db → SQLite database created by the script.

sales_summary.py → Example query + chart.

📊 Example Output
=================

Terminal Output
-------------------
product	total_qty	revenue
Laptop	2	1500.0
Phone	3	1200.0
Headphones	5	300.0

Bar Chart
-------------
<img width="1180" height="780" alt="image" src="https://github.com/user-attachments/assets/f7c884bc-b24e-4025-b13e-3c3d0e442ed3" />


📌 Why This Matters

This is your foundation — before you can analyze or visualize sales data, you need a clean, structured way to store it.
Once the database is ready, you can:

Write SQL queries to summarize revenue or quantities sold.

Use Pandas to make the results look nice.

Make visual charts with Matplotlib.
