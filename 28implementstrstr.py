class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        return haystack.find(needle)

s = Solution()

print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))

