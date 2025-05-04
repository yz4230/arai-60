from itertools import product


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
        for candidate in candidates:
            if target < candidate:
                continue
            dp[candidate].append([candidate])
        for i in range(1, target + 1):
            added = set[tuple]()
            for j in range(1, i // 2 + 1):
                for a, b in product(dp[j], dp[i - j]):
                    tup = tuple(sorted(a + b))
                    if tup not in added:
                        dp[i].append(a + b)
                        added.add(tup)
        return dp[-1]


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
