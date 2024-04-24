#https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        map = {}

        if len(pattern) != len(s_words):
            return False

        for i in range(len(pattern)):
            try:
                if map[pattern[i]] != s_words[i]:
                    return False
            except KeyError:
                if s_words[i] in map.values():
                    return False

                map[pattern[i]] = s_words[i]

        return True

s = Solution()
print(s.wordPattern("aaa","aa aa aa aa"), False)
print(s.wordPattern("abba","dog dog dog dog" ), False)
print(s.wordPattern("abba","dog cat cat dog" ), True)
print(s.wordPattern("abba","dog cat cat fish" ), False)
print(s.wordPattern("aaaa","dog cat cat dog" ), False)