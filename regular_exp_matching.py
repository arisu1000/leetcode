import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rep = re.compile(p)
        result = rep.match(s)
        
        if result == None:
            return False
        if result.group() == s:
            return True
        return False

s = Solution()

print(s.isMatch("aa", "a"), False)
print(s.isMatch("aa", "a*"), True)
print(s.isMatch("aa", ".*"), True)
print(s.isMatch("aab", "c*a*b"), True)
print(s.isMatch("mississippi", "mis*is*p*."), False)