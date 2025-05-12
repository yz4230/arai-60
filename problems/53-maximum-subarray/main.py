class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        ans = -(10**10)
        bottom = 0
        for n in nums:
            total += n
            ans = max(ans, total - bottom)
            bottom = min(bottom, total)

        return ans


print(Solution().maxSubArray(nums=[-2, 1]))
