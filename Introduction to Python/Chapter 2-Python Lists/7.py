# Exercise
# Exercise
# Slicing and dicing (2)
# In the video, Filip first discussed the syntax where you specify both where to begin and end the slice of your list:

# my_list[begin:end]
# However, it's also possible not to specify these indexes. If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

# x = ["a", "b", "c", "d"]
# x[:2]
# x[2:]
# x[:]
# Instructions
# 100 XP
# Instructions
# 100 XP
# Create downstairs again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
# Create upstairs again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]