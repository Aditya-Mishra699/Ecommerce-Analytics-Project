import sqlite3
import pandas as pd

# Load CSV file
df = pd.read_csv("supermarket.csv")

# Connect to database
conn = sqlite3.connect("supermarket.db")

# Create SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Table created successfully!")


query = """
SELECT name 
FROM sqlite_master 
WHERE type='table';
"""

df = pd.read_sql_query(query, conn)

print(df)


# ------------------------------------------------
# Query 1: First 10 Rows
# ------------------------------------------------
query1 = """
SELECT * 
FROM sales 
LIMIT 10
"""

df1 = pd.read_sql_query(query1, conn)

print("\nFIRST 10 ROWS:")
print(df1)

# ------------------------------------------------
# Query 2: Total Revenue
# ------------------------------------------------
query2 = """
SELECT SUM(Sales) AS Total_Revenue
FROM sales
"""

df2 = pd.read_sql_query(query2, conn)

print("\nTOTAL REVENUE:")
print(df2)

# ------------------------------------------------
# Query 3: Revenue by Category
# ------------------------------------------------
query3 = """
SELECT Category, SUM(Sales) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC
"""

df3 = pd.read_sql_query(query3, conn)

print("\nREVENUE BY CATEGORY:")
print(df3)

# ------------------------------------------------
# Query 4: Average Sales
# ------------------------------------------------
query4 = """
SELECT AVG(Sales) AS Average_Sales
FROM sales
"""

df4 = pd.read_sql_query(query4, conn)

print("\nAVERAGE SALES:")
print(df4)

# ------------------------------------------------
# Query 5: Total Orders
# ------------------------------------------------
query5 = """
SELECT COUNT(*) AS Total_Orders
FROM sales
"""

df5 = pd.read_sql_query(query5, conn)

print("\nTOTAL ORDERS:")
print(df5)

# ------------------------------------------------
# Query 6: Highest Sale
# ------------------------------------------------
query6 = """
SELECT MAX(Sales) AS Highest_Sale
FROM sales
"""

df6 = pd.read_sql_query(query6, conn)

print("\nHIGHEST SALE:")
print(df6)

# ------------------------------------------------
# Query 7: Lowest Sale
# ------------------------------------------------
query7 = """
SELECT MIN(Sales) AS Lowest_Sale
FROM sales
"""

df7 = pd.read_sql_query(query7, conn)

print("\nLOWEST SALE:")
print(df7)

# ------------------------------------------------
# Query 8: Sales Greater Than 500
# ------------------------------------------------
query8 = """
SELECT *
FROM sales
WHERE Sales > 500
"""

df8 = pd.read_sql_query(query8, conn)

print("\nSALES GREATER THAN 500:")
print(df8)

# ------------------------------------------------
# Query 9: Average Sales by Category
# ------------------------------------------------
query9 = """
SELECT Category, AVG(Sales) AS Avg_Sales
FROM sales
GROUP BY Category
ORDER BY Avg_Sales DESC
"""

df9 = pd.read_sql_query(query9, conn)

print("\nAVERAGE SALES BY CATEGORY:")
print(df9)

# Close connection
conn.close()
