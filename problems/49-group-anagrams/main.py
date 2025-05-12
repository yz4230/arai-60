class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[str, list[str]] = {}

        for s in strs:
            h = str(sorted(list(s)))
            anagrams[h] = anagrams.get(h, []) + [s]

        return list(anagrams.values())
