from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> list[list[int]]:
        visited = set[tuple[int, int]]()
        pq: list[tuple[int, tuple[int, int]]] = []
        pq.append((nums1[0] + nums2[0], (0, 0)))
        ret: list[list[int]] = []
        for _ in range(k):
            _, (i, j) = heappop(pq)
            ret.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1:
                pos = (i + 1, j)
                if pos not in visited:
                    visited.add(pos)
                    heappush(pq, (nums1[i + 1] + nums2[j], pos))
            if j < len(nums2) - 1:
                pos = (i, j + 1)
                if pos not in visited:
                    visited.add(pos)
                    heappush(pq, (nums1[i] + nums2[j + 1], pos))
        return ret
