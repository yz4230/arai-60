class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 1
        while 0 < i and nums[i] <= nums[i - 1]:
            i -= 1

        if i > 0:
            j = len(nums) - 1
            while i < j and nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])
