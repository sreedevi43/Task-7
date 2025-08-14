import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#  To connect to the  database
conn = sqlite3.connect("sales_data.db")

#  to run the sql query
query = """
SELECT
  product,
  SUM(quantity) AS total_qty,
  SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""
df = pd.read_sql_query(query, conn)

# print the results
print("Sales Summary (by Product):")
print(df)

# plot the bar chart
plt.figure()
plt.bar(df["product"], df["revenue"])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("sales_chart.png", dpi=150)  # save the chart
plt.show()

# close the connection
conn.close()
