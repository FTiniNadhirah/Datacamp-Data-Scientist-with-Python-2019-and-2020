# Pandas and The Hello World of SQL Queries!
# Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one swift line of Python code!

# You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. Then you'll query the database to select all records from the Album table.

# Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following command:

# df = pd.read_sql_query("SELECT * FROM Orders", engine)
# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the pandas package using the alias pd.
# Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
# Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the table Album.
# The remainder of the code is included to confirm that the DataFrame created by this method is equal to that created by the previous method that you learned.

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))