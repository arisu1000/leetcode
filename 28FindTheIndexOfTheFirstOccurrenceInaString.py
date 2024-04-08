#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstIndex = -1

        i = 0
        while i < len(haystack):

            j = 0
            tmpi = i
            while j < len(needle):
                try:
                    if haystack[tmpi] == needle[j]:
                        if j == 0:
                            firstIndex = tmpi

                        tmpi += 1
                        j += 1
                    else:
                        break
                
                    if j == len(needle):
                        return firstIndex
                except IndexError:
                    return -1
            i += 1
                
        return -1



s = Solution()


print(s.strStr("sadbutsad", "sad"), 0)
print(s.strStr("leetcode", "leeto"), -1)
print(s.strStr("hello", "ll"), 2)
print(s.strStr("aaaaa", "bba"), -1)
print(s.strStr("aaa", "aaaa"), -1)
print(s.strStr("mississippi", "issip"), 4)
