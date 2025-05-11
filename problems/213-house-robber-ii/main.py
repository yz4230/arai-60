class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_inner(nums: list[int]) -> int:
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[-1]

        return max(rob_inner(nums[:-1]), rob_inner(nums[1:]))
