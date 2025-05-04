class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        patterns: list[list[int]] = []
        for i, n in enumerate(nums):
            for pat in self.permute(nums[:i] + nums[i + 1 :]):
                patterns.append([n] + pat)
        return patterns
