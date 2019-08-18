# Add conditionals
# The while loop that corrects the offset is a good start, but what if offset is negative? You can try to run the following code where offset is initialized to -6:

# # Initialize offset
# offset = -6

# # Code the while loop
# while offset != 0 :
    # print("correcting...")
    # offset = offset - 1
    # print(offset)
# but your session will be disconnected. The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.

# Fix things by putting an if-else statement inside the while loop. If your code is still taking too long to run, you probably made a mistake!

# Instructions
# 100 XP
# Inside the while loop, replace offset = offset - 1 by an if-else statement:
# If offset is greater than zero, you should decrease offset by 1.
# Else, you should increase offset by 1.
# If you've coded things correctly, hitting Submit Answer should work this time. If your code is still taking too long to run, you probably made a mistake!

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    
    print(offset)
