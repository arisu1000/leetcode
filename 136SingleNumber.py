# https://leetcode.com/problems/single-number

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
                if count == 2:
                    tmp = nums[i]
                    count = 1
                else:
                    return tmp
        
        return nums[len(nums)-1]

            

    
s = Solution()

print(s.singleNumber([4,1,2,1,2]), 4)
print(s.singleNumber([2,2,1]), 1)
print(s.singleNumber([1]), 1)