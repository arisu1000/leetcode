from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_s = 200
        len_strs = len(strs)
        for s in strs:
            len_s = len(s)
            if len_s < min_s:
                min_s = len_s

        find_prefix = ""
        for i in range(0, min_s):
            char = strs[0][i]
            for j in range(1, len_strs):
                if char != strs[j][i]:
                    return find_prefix
            
            find_prefix += char

        return find_prefix

s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))

