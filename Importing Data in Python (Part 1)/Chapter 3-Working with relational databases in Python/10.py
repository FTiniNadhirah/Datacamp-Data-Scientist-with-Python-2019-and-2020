# Filtering your INNER JOIN
# Congrats on performing your first INNER JOIN! You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.

# Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:

# "SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"
# The following code has already been executed to import the necessary packages and to create the engine:

# import pandas as pd
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///Chinook.sqlite')
# Instructions
# 100 XP
# Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000.
# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)

# Print head of DataFrame
print(df.head())