class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cursor = 0
        while cursor < len(t) and len(s) > 0:
            if s[0] == t[cursor]:
                s = s[1:]
            cursor += 1
        return len(s) == 0
