#https://leetcode.com/problems/jump-game/description

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        
        targetIndex = length - 1
        moveIndex = targetIndex - 1
        isPossible = True
        while moveIndex >= 0:
            if moveIndex + nums[moveIndex] >= targetIndex:
                targetIndex = moveIndex
                moveIndex -= 1
                isPossible = True
            else:
                moveIndex -= 1
                isPossible = False

        return isPossible


s = Solution()
print(s.canJump([2,3,1,1,4]))
              #  0,1,2,3,4
print(s.canJump([3,2,1,0,4]))
print(s.canJump([0]))
print(s.canJump([0, 1])) #false
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))