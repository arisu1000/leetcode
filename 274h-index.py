#https://leetcode.com/problems/h-index

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        hindex = 0
        for i, val in enumerate(citations, 0):
            if i < val:
                hindex += 1

        return hindex

s = Solution()
print(s.hIndex([3,0,6,1,5]), 3)
print(s.hIndex([1,3,1]), 1)
print(s.hIndex([1]), 1)
print(s.hIndex([0]), 0)
print(s.hIndex([11, 15]), 2)
