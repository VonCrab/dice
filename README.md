# dice
## A simple dice rolling simulator project

Based of the specification found here: [https://www.reddit.com/r/beginnerprojects/comments/1j50e7/project_dice_rolling_simulator/]

I had an additional goal of making the code 'module' friendly. Meaning it could be lightweight and easily imported into other projects.

### Breakdown of dice module components

1. dice.roll(x): Takes x as a number of sides on a dice and returns an int between 1 and x inclusively.

2. dice.dice_sim(x, y): Takes a number of sides per dice x and number of dice to roll y. Returns a dictionary of sides to number of rolls (side -> rolls)

3. percent_appears(dict): Takes a dict with (side -> rolls) and returns a copy of the same dict with a tuple representing the number of times a side was rolls and percent of total rolls. {side: (number of rolls, percent of total)}

4. isint(x): Internal function used to determine if a user input is a valid postive interger. Returns a boolean.

5. main(): For use when the module is run independently. Asks a user for a number of sides and number of rolls. Prints the info from percent_appears. User can do multiple loops sims.
