#! /usr/bin/env python

from BowlingGame import BowlingGame
import unittest2 as unittest

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = BowlingGame()

    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5)

    def rollStrike(self):
        self.g.roll(10)

    def rollMany(self, n, pins):
        for _ in xrange(0, n):
            self.g.roll(pins)

    def testGutterGame(self):
        self.rollMany(20, 0)

        self.assertEquals(0, self.g.gamescore())

    def testAllOnes(self):
        self.rollMany(20, 1)

        self.assertEquals(20, self.g.gamescore())

    def testOneSpare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17, 0)

        self.assertEquals(16, self.g.gamescore())

    def testOneStrike(self):
        self.rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16, 0)

        self.assertEquals(24, self.g.gamescore())

    def testPerfectGame(self):
        self.rollMany(12, 10)

        self.assertEquals(300, self.g.gamescore())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2, buffer=True)
