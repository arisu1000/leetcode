#https://leetcode.com/problems/reverse-words-in-a-string


class Solution:
    def reverseWords(self, s: str) -> str:
        splits = s.split()

        reserved = ""
        for i in range(len(splits) - 1, -1,  -1):
            reserved += splits[i] + " "

        return reserved[0:len(reserved) - 1]
        


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("world hello"))
print(s.reverseWords("a good   example"))