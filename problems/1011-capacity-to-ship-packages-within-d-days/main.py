class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2  # mininum capacity candidate

            cursor = 0
            current_load = 0
            required_days = 0
            while cursor < len(weights):
                if current_load + weights[cursor] > mid:
                    current_load = weights[cursor]
                    required_days += 1
                else:
                    current_load += weights[cursor]
                cursor += 1
            if current_load > 0:
                required_days += 1

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left
