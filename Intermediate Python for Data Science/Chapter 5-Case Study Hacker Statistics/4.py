# The next step
# Before, you have already written Python code that determines the next step based on the previous step. Now it's time to put this code inside a for loop so that we can simulate a random walk.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.

# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
