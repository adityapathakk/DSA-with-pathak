class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxBottles = numBottles
        while numBottles >= numExchange:
            maxBottles += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return maxBottles


""" Approach

first, we set max bottles to be at least the number of bottles.
then, as long as numBottles (number of bottles that're full) is >= numExchange (number of bottles required for exchange),
we can perform integer division (numBottles // numExchange) to find out how many bottles can be added after exchanging.
'numBottles' gets updated -- the remainder of (numBottles // numExchange) is added, too.

"""
