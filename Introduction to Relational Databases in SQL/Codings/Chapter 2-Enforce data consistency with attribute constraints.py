# Exercise
# Conforming with data types
# For demonstration purposes, I created a fictional database table that only holds three records. The columns have the data types date, integer, and text, respectively.

# CREATE TABLE transactions (
 # transaction_date date, 
 # amount integer,
 # fee text
# );
# Have a look at the contents of the transactions table.

# The transaction_date accepts date values. According to the PostgreSQL documentation, it accepts values in the form of YYYY-MM-DD, DD/MM/YY, and so forth.

# Both columns amount and fee appear to be numeric, however, the latter is modeled as text – which you will account for in the next exercise.

# Instructions

# Execute the given sample code.
# As it doesn't work, have a look at the error message and correct the statement accordingly – then execute it again.

-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('2018-09-24', 5454, '30');

-- Doublecheck the contents
SELECT *
FROM transactions;

# Exercise
# Type CASTs
# In the video, you saw that type casts are a possible solution for data type issues. If you know that a certain column stores numbers as text, you can cast the column to a numeric form, i.e. to integer.

# SELECT CAST(some_column AS integer)
# FROM table;
# Now, the some_column column is temporarily represented as integer instead of text, meaning that you can perform numeric calculations on the column.

# Instructions

# Execute the given sample code.
# As it doesn't work, add an integer type cast at the right place and execute it again.
-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;

# Exercise
# Change types with ALTER COLUMN
# The syntax for changing the data type of a column is straightforward. The following code changes the data type of the column_name column in table_name to varchar(10):

# ALTER TABLE table_name
# ALTER COLUMN column_name
# TYPE varchar(10)
# Now it's time to start adding constraints to your database.

# Instructions 1/3
# Have a look at the distinct university_shortname values and take note of the length of the strings.
-- Select the university_shortname column
SELECT DISTINCT(university_shortname) 
FROM professors;

# Instructions 2/3
# Now specify a fixed-length character type with the correct length for university_shortname.
-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

# Instructions 3/3
# Change the type of the firstname column to varchar(64).
-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

# Exercise
# Convert types USING a function
# If you don't want to reserve too much space for a certain varchar column, you can truncate the values before converting its type.

# For this, you can use the following syntax:

# ALTER TABLE table_name
# ALTER COLUMN column_name
# TYPE varchar(x)
# USING SUBSTRING(column_name FROM 1 FOR x)
# You should read it like this: Because you want to reserve only x characters for column_name, you have to retain a SUBSTRING of every value, i.e. the first x characters of it, and throw away the rest. This way, the values will fit the varchar(x) requirement.

# Instructions

# Run the sample code as is and take note of the error.
# Now use SUBSTRING() to reduce firstname to 16 characters so its type can be altered to varchar(16).
-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors 
ALTER COLUMN firstname 
TYPE varchar(16) 
USING SUBSTRING(firstname FROM 1 FOR 16);

# Exercise
# Disallow NULL values with SET NOT NULL
# The professors table is almost ready now. However, it still allows for NULLs to be entered. Although some information might be missing about some professors, there's certainly columns that always need to be specified.

# Instructions 1/2

# Add a not-null constraint for the firstname column.
-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

# Instructions 2/2

# Add a not-null constraint for the lastname column.
-- Disallow NULL values in lastname
ALTER TABLE professors 
ALTER COLUMN lastname SET NOT NULL;

# Exercise
# Make your columns UNIQUE with ADD CONSTRAINT
# As seen in the video, you add the UNIQUE keyword after the column_name that should be unique. This, of course, only works for new tables:

# CREATE TABLE table_name (
 # column_name UNIQUE
# );
# If you want to add a unique constraint to an existing table, you do it like that:

# ALTER TABLE table_name
# ADD CONSTRAINT some_name UNIQUE(column_name);
# Note that this is different from the ALTER COLUMN syntax for the not-null constraint. Also, you have to give the constraint a name some_name.

# Instructions 1/2

# Add a unique constraint to the university_shortname column in universities. Give it the name university_shortname_unq.
-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

# Instructions 2/2

# Add a unique constraint to the organization column in organizations. Give it the name organization_unq.
-- Make organizations.organization unique
ALTER TABLE organizations
ADD CONSTRAINT organization_unq UNIQUE(organization);