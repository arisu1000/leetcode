# https://leetcode.com/problems/plus-one

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = ""
        for n in digits:
            s += str(n)
        
        tmp = str(int(s) + 1)
        result = []
        for c in tmp:
            result.append(int(c))

        return result

s = Solution()
print(s.plusOne([1,2,3]), [1,2,4])
print(s.plusOne([4,3,2,1]), [4,3,2,2])
print(s.plusOne([9]), [1,0])