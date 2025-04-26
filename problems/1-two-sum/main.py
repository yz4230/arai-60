class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices: dict[int, int] = {}
        for i, num in enumerate(nums):
            indices[num] = i
        for i in range(len(nums)):
            b = target - nums[i]
            if b in indices and indices[b] != i:
                return sorted([i, indices[b]])
        raise ValueError()
