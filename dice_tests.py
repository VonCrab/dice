#! /usr/bin/python

import unittest
import dice

class SingleDiceTest(unittest.TestCase):

    def test_roller(self):
        self.assertIn(dice.roll(3), range(1,4))
        self.assertIn(dice.roll(6), range(1,7))
        self.assertIn(dice.roll(12), range(1,13))
        self.assertIn(dice.roll(15), range(1,16))
        self.assertIn(dice.roll(25), range(1,26))

class MultipleDiceTest(unittest.TestCase):

    def tearDown(self):
        self.rolled = None

    def test_roll2(self):
        self.rolled = dice.dice_sim(3, 2)

        self.assertNotEqual(len(self.rolled), 0)

        for side in self.rolled.keys():
            self.assertIn(side, range(1,4))

    def test_roll6(self):
        self.rolled = dice.dice_sim(6, 6)


        self.assertNotEqual(len(self.rolled), 0)

        for side in self.rolled.keys():
            self.assertIn(side, range(1,7))


    def test_many_rolls(self):
        self.rolled = dice.dice_sim(25, 1000)


        self.assertNotEqual(len(self.rolled), 0)

        for side in self.rolled.keys():
            self.assertIn(side, range(1, 26))

class PercentDiceTest(unittest.TestCase):

    def test_d3(self):
        test_rolls = {1: 1, 2: 1, 3: 1}

        results = dice.percent_appears(test_rolls)

        self.assertEqual(results, {1: (1, 33.33), 2: (1, 33.33), 3: (1, 33.33)})

    def test_d6(self):
        test_rolls = {1: 5, 3: 3, 5: 2, 6: 10}

        results = dice.percent_appears(test_rolls)

        self.assertEqual(results, {1: (5, 25.00), 3: (3, 15.00), 5: (2, 10.00), 6: (10, 50.00)})

if __name__ == '__main__':
    unittest.main()
