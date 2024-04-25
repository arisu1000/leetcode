#https://leetcode.com/problems/group-anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}
        for str in strs:
            key = ''.join(sorted(str))

            try:
                ans[key].append(str)
            except KeyError:
                ans[key] = []
                ans[key].append(str)
                
        result = []
        for key, value in ans.items():
            result.append(value)

        return result


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams(["",""]), [["",""]])