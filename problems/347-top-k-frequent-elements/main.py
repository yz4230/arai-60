from collections import Counter
from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        topk = list[tuple[int, int]]()
        for val, cnt in counter.items():
            heappush(topk, (cnt, val))
            if len(topk) > k:
                heappop(topk)
        return [val for _, val in topk]
