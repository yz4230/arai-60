class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        if neg:
            n = -n
        ans = 1.0
        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2
        if neg:
            return 1 / ans
        return ans


sol = Solution()
print(sol.myPow(2, -3))
