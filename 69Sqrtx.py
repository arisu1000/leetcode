# https://leetcode.com/problems/sqrtx

import math

class Solution:
    def mySqrt(self, x: int) -> int:

        result = math.sqrt(x)

        return int(result)
    
s = Solution()
print(s.mySqrt(4), 2)
print(s.mySqrt(8), 2)