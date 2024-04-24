#https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map = {}
        for i in range(len(s)):
            try:
                if map[s[i]] != t[i]:
                    return False

            except KeyError:
                if t[i] in  map.values():
                    return False

                map[s[i]] = t[i]

        return True
            


s = Solution()
print(s.isIsomorphic("badc", "baba"), False)
print(s.isIsomorphic("egg", "add"), True)
print(s.isIsomorphic("foo", "bar"), False)
print(s.isIsomorphic("paper", "title"), True)
