#! /usr/bin/python

import random

# User input: a real number for the sides of a dice
# User input: a real number for the amount of times to be rolled

# Output: a random int from the faces rolled
# Final output: a print out of all the times a face was rolled


# Option 1: generate a list of each dice face, sample the list
# Option 2: generate a random int for a range based on faces

# Subgoals: User inputs = real numbers only
# Subgoals: Allow the user to keep rolling without have to x program
# Subgoals: Percentage each side appeared

def roll(sides):
    return random.randint(1, sides)
