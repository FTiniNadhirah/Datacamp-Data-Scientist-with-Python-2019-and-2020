# Exercise
# Query information_schema with SELECT
# information_schema is a meta-database that holds information about your current database. information_schema has multiple tables you can query with the known SELECT * FROM syntax:

# tables: information about all tables in your current database
# columns: information about all columns in all of the tables in your current database

# In this exercise, you'll only need information from the 'public' schema, which is specified as the column table_schema of the tables and columns tables. The 'public' schema holds information about user-defined tables and databases. The other types of table_schema hold system information – for this course, you're only interested in user-defined stuff.

# Instructions 1/4

# Get information on all table names in the current database, while limiting your query to the 'public' table_schema.

-- Query the right table in information_schema
SELECT table_name 
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';

# Instructions 2/4

# Now have a look at the columns in university_professors by selecting all entries in information_schema.columns that correspond to that table.
-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns
WHERE table_name = 'university_professors' AND table_schema = 'public';

# Instructions 4/4

# Finally, print the first five rows of the university_professors table.
-- Query the first five rows of our table
SELECT * 
FROM university_professors 
LIMIT 5;

# Exercise
# CREATE your first few TABLEs
# You'll now start implementing a better database model. For this, you'll create tables for the professors and universities entity types. The other tables will be created for you.

# The syntax for creating simple tables is as follows:

# CREATE TABLE table_name (
 # column_a data_type,
 # column_b data_type,
 # column_c data_type
# );
# Attention: Table and columns names, as well as data types, don't need to be surrounded by quotation marks.

# Instructions 1/2
# Create a table professors with two text columns: firstname and lastname.
-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT * 
FROM professors

# Instructions 2/2
# Create a table universities with three text columns: university_shortname, university, and university_city.
-- Create a table for the universities entity type
CREATE TABLE universities (
 university_shortname text,
 university text,
 university_city text
);
-- Print the contents of this table
SELECT * 
FROM universities

# Exercise
# ADD a COLUMN with ALTER TABLE
# Oops! We forgot to add the university_shortname column to the professors table. You've probably already noticed:



# In chapter 4 of this course, you'll need this column for connecting the professors table with the universities table.

# However, adding columns to existing tables is easy, especially if they're still empty.

# To add columns you can use the following SQL query:

# ALTER TABLE table_name
# ADD COLUMN column_name data_type;
# Instructions

# Alter professors to add the text column university_shortname.

-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors

# Exercise
# RENAME and DROP COLUMNs in affiliations
# As mentioned in the video, the still empty affiliations table has some flaws. In this exercise, you'll correct them as outlined in the video.

# You'll use the following queries:

# To rename columns:
# ALTER TABLE table_name
# RENAME COLUMN old_name TO new_name;
# To delete columns:
# ALTER TABLE table_name
# DROP COLUMN column_name;

# Instructions 1/2
# Rename the organisation column to organization in affiliations.
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

# Instructions 2/2

# Delete the university_shortname column in affiliations.
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;

# Exercise
# Migrate data with INSERT INTO SELECT DISTINCT
# Now it's finally time to migrate the data into the new tables. You'll use the following pattern:

# INSERT INTO ... 
# SELECT DISTINCT ... 
# FROM ...;
# It can be broken up into two parts:

# First part:

# SELECT DISTINCT column_name1, column_name2, ... 
# FROM table_a;
# This selects all distinct values in table table_a – nothing new for you.

# Second part:

# INSERT INTO table_b ...;
# Take this part and append it to the first, so it inserts all distinct rows from table_a into table_b.

# One last thing: It is important that you run all of the code at the same time once you have filled out the blanks.

# Instructions 1/2

# Insert all DISTINCT professors from university_professors into professors.
# Print all the rows in professors.

# Insert all DISTINCT affiliations into affiliations.
-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

# Instructions 2/2

# Insert all DISTINCT affiliations into affiliations.
-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;

# Exercise
# Delete tables with DROP TABLE
# Obviously, the university_professors table is now no longer needed and can safely be deleted.

# For table deletion, you can use the simple command:

# DROP TABLE table_name;
# Instructions

# Delete the university_professors table.
-- Delete the university_professors table
DROP TABLE university_professors;