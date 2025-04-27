import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        for _ in range(len(self.nums) - k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
