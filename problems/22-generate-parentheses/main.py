class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp: list[list[list[str]]] = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = [""]

        for i in range(n):  # i pushes
            # move left
            for j in range(i + 1):  # j pops
                dp[i + 1][j] = [pat + "(" for pat in dp[i][j]]
            # move down
            for j in range(i + 1):
                dp[i + 1][j + 1] += [pat + ")" for pat in dp[i + 1][j]]

        return dp[-1][-1]


sol = Solution()
print(sol.generateParenthesis(3))
