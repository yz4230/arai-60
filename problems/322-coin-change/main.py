class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [10**5] * (10**4 + 1)
        dp[0] = 0

        for current in range(len(dp)):
            for coin in coins:
                if current + coin < len(dp):
                    dp[current + coin] = min(dp[current + coin], dp[current] + 1)

        if dp[amount] == 10**5:
            return -1

        return dp[amount]
