class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        match len(s):
            case 0:
                return 0
            case 1:
                return 1

        chars = set()
        chars.add(s[0])
        tail, head = 0, 1
        result = 0
        while head < len(s):
            if s[head] in chars:
                chars.remove(s[tail])
                tail += 1
            else:
                chars.add(s[head])
                head += 1
            result = max(result, head - tail)
        return result
