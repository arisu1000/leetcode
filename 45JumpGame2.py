#https://leetcode.com/problems/jump-game-ii/description

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        
        targetIndex = length - 1
        moveIndex = targetIndex - 1
        countStep = 0
        tmpIndex = 10000000
        while moveIndex >= 0 and tmpIndex > 0:
            if moveIndex + nums[moveIndex] >= targetIndex:
                tmpIndex = moveIndex
            
            moveIndex -= 1
            
            if moveIndex < 0:
                targetIndex = tmpIndex
                moveIndex = tmpIndex - 1
                countStep += 1

        return countStep


s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))
print(s.jump([0]))
print(s.jump([3,2,1]))
