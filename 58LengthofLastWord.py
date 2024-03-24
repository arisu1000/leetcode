

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_splits = s.split()
        n = len(s_splits)
        return len(s_splits[n-1])
    

s = Solution()
# print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))



