class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices[1:]:
            # buy = min(buy, price)
            if buy > price: buy = price
            profit = max(profit, price - buy)
        return profit