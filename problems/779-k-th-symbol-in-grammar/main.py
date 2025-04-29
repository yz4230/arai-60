class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.solve(n - 1, k - 1)

    def solve(self, n: int, k: int):
        if n == 0:
            return 0
        prev = self.solve(n - 1, k >> 1)
        if prev == 0:
            return [0, 1][k & 0b1]
        if prev == 1:
            return [1, 0][k & 0b1]
        raise ValueError()
