#! /usr/bin/python

import unittest
import rolling_sim

class SingleDiceTest(unittest.TestCase):

    def test_roller(self):
        self.assertIn(rolling_sim.roll(3), range(1,4))
        self.assertIn(rolling_sim.roll(6), range(1,6))
        self.assertIn(rolling_sim.roll(12), range(1,12))
        self.assertIn(rolling_sim.roll(15), range(1,15))
        self.assertIn(rolling_sim.roll(25), range(1,25))


if __name__ == '__main__':
    unittest.main()
