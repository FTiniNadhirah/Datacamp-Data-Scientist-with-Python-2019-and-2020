# Exercise
# Exercise
# Driving right (2)
# The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.

# Instructions
# 100 XP
# Convert the code on the right to a one-liner that calculates the variable sel as before.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]

# Print sel
print(sel)