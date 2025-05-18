from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        assert len(beginWord) == len(endWord)
        n = len(beginWord)

        skipped_words = dict[str, list[str]]()  # { "dog": ["og", "dg", "do"] }
        for word in [*wordList, beginWord]:
            words = []
            for skip_idx in range(n):
                words.append(word[:skip_idx] + word[skip_idx + 1 :])
            skipped_words[word] = words

        db = dict[int, dict[str, list[str]]]()  # { 0: { "og": ["dog", "log", "cog"] } }
        for skip_idx in range(n):
            skip_db = dict[str, list[str]]()
            for word in wordList:
                skipped = word[:skip_idx] + word[skip_idx + 1 :]
                if skipped not in skip_db:
                    skip_db[skipped] = []
                skip_db[skipped].append(word)
            db[skip_idx] = skip_db

        queue = deque[tuple[str, int]]()  # (word, depth)
        queue.append((beginWord, 1))
        visited = set[str]()
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            for skip_idx in range(n):
                part = skipped_words[word][skip_idx]
                skip_db = db[skip_idx]
                for word2 in skip_db.get(part, {}):
                    if word2 not in visited:
                        visited.add(word2)
                        queue.append((word2, depth + 1))
        return 0


print(
    Solution().ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
