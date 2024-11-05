# https://leetcode.com/problems/single-number-ii

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums.sort()
        tmp = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == tmp:
                count += 1    
            else:
                if count == 3:
                    tmp = nums[i]
                    count = 1
                else:
                    return tmp

        return tmp
    
s = Solution()
print(s.singleNumber([2,2,3,2]), 3)
print(s.singleNumber([0,1,0,1,0,1,99]), 99)