class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                if dp[i] and s[i:j] in words:
                    dp[j] = True
        return dp[len(s)]


sol = Solution()
print(sol.wordBreak(s="aaaaaaaa", wordDict=["aaaa", "aaa"]))
