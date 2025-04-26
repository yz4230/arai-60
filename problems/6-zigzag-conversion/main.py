from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ""
        zs = ceil(len(s) / numRows)
        for row in range(numRows):
            if row == 0:
                result += s[:: 2 * numRows - 2]
            elif row == numRows - 1:
                result += s[numRows - 1 :: 2 * numRows - 2]
            else:
                for zigs in range(zs):
                    zig = 2 * (numRows - 1)
                    left = zig * zigs + row
                    if left < len(s):
                        result += s[left]
                    right = zig * (zigs + 1) - row
                    if right < len(s):
                        result += s[right]
        return result
