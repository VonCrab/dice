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

# TODO: Check that input values are > 0

def roll(sides):
    '''
    Returns a pesudo-random integer within the bounds of 1 to sides. Assumes sides is a non-negative integer.

    Used to simulate a single dice rolls.

    Takes a single argument sides, which is assumed to be an int > 0.
    '''
    return random.randint(1, sides)

def dice_sim(sides, num_of_dice):
    """
    Returns a dictionary of rolls after running a simulation of rolling a specified number of dice.

    Assumes arguments sides and number of dice are ints > 0.
    """
    rolls = {}

    while 0 < num_of_dice:
        temp = roll(sides)

        rolls[temp] = rolls.get(temp, 0) + 1

        num_of_dice -= 1

    return rolls

def percent_appears(rolls):
    """
    Returns a dictionary of sides -> (number of times rolled, percent of times rolled)

    Assumes rolls is a valid dict of sides -> times rolled.
    """
    total = float(sum(rolls.values()))

    for side in rolls:
        percent = round(rolls[side] / total * 100, 2)

        rolls[side] = (rolls[side], percent)

    return rolls

# TODO: craft the main function for the user
# TODO: Needs to include the ability to take and check real numbers
# TODO: Needs to have an infinite loop that the user can keep rolling
