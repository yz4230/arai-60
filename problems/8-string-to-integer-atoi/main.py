class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        cursor = 0

        # ignore leading spaces
        while cursor < len(s) and s[cursor] == " ":
            cursor += 1

        if cursor == len(s):
            return 0

        # negative, otherwise positive
        neg = False
        if s[cursor] == "+":
            cursor += 1
        elif s[cursor] == "-":
            neg = True
            cursor += 1

        # ignore leading zeros
        while cursor < len(s) and s[cursor] == "0":
            cursor += 1

        if cursor == len(s):
            return 0

        MIN = 2**31
        MAX = 2**31 - 1

        ret = 0
        while cursor < len(s):
            if not (ord("0") <= ord(s[cursor]) <= ord("9")):
                break
            digit = ord(s[cursor]) - ord("0")
            if neg and (MIN - digit) / 10 < ret:
                ret = MIN
                break
            if not neg and (MAX - digit) / 10 < ret:
                ret = MAX
                break
            ret = ret * 10 + digit
            cursor += 1

        if neg:
            return -ret
        return ret


sol = Solution()
print(sol.myAtoi("   -042"))
