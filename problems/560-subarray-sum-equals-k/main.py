class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        psum = {0: 1}
        current_sum = 0
        count = 0

        for n in nums:
            current_sum += n
            count += psum.get(current_sum - k, 0)
            psum[current_sum] = psum.get(current_sum, 0) + 1

        return count
