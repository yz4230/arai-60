class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        lowest = 10**5
        for price in prices:
            max_profit = max(max_profit, price - lowest)
            lowest = min(price, lowest)
        return max_profit
