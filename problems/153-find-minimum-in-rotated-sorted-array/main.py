class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[0] <= nums[mid]:  # last
                left = mid + 1
            else:
                right = mid
        return nums[left]
