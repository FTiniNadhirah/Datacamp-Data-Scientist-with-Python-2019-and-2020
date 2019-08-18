# Exercise
# Exercise
# Replace list elements
# Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

# Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

# x = ["a", "b", "c", "d"]
# x[1] = "r"
# x[2:] = ["s", "t"]
# For this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a house.

# Instructions
# 100 XP
# Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
# Make the areas list more trendy! Change "living room" to "chill zone".
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.5
print(areas)

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)