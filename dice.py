#! /usr/bin/python

import random

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

def _isint(val):
    """
    Returns if an input is a valid postive int
    """
    try:
        val = int(val)
    except ValueError:
        return False
    else:
        return True

def main():
    print("Dice Rolling Simulator loaded...")

    while True:

        print("Enter 'x' to quit at anytime.")

        sides = raw_input("Please enter the number of sides on a dice: ")

        if sides == 'x':
            break
        elif _isint(sides) and 0 < int(sides):
            sides = int(sides)
        else:
            print("Please enter a postive interger for the sides of the dice.\n")
            continue

        num_of_dice = raw_input("Please enter the number of dice to roll: ")

        if num_of_dice == 'x':
            break
        elif _isint(num_of_dice) and 0 < int(num_of_dice):
            num_of_dice = int(num_of_dice)
        else:
            print("Please enter a positive interger for the number of rolls.\n")


        rolls = dice_sim(sides, num_of_dice)

        # returns {SIDE: (NUM OF TIMES ROLLED, PERCENT OF TOTAL ROLLS)}
        rolls_percents = percent_appears(rolls)

        for side in rolls_percents:
            print("Side %d: " % side),
            print("%d total rolls, " % rolls_percents[side][0]),
            print("%0.2f percent of rolls" % rolls_percents[side][1])

        print

if __name__ == '__main__':
    main()
