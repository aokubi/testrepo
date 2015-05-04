#! /usr/bin/env python

class BowlingGame(object):

    def __init__(self):
        self.rolls = [None] * 20
        self.currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def gamescore(self):
        score = 0
        frameIndex = 0
        for _ in xrange(0, 10):
            if self.isStrike(frameIndex):
                score += 10 + self.strikeBonus(frameIndex)
                frameIndex += 1
            elif self.isSpare(frameIndex):
                score += 10 + self.spareBonus(frameIndex)
                frameIndex += 2
            else:
                score += self.sumOfBallsInFrame(frameIndex)
                frameIndex += 2

        return score

    def sumOfBallsInFrame(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex + 2]

    def strikeBonus(self, frameIndex):
        return self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]

    def isSpare(self, frameIndex):
        return (self.rolls[frameIndex] + self.rolls[frameIndex + 1]) == 10

    def isStrike(self, frameIndex):
        return self.rolls[frameIndex] == 10
