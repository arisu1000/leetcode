# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums) - 1
        findLeft, findRight = False, False
        result = [-1, -1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                result[0] = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                result[1] = i
                break

        return result
    

s = Solution()

print(s.searchRange([1], 1), [0, 0])
print(s.searchRange([5,7,7,8,8,10], 8), [3,4])
print(s.searchRange([5,7,7,8,8,10], 6), [-1,-1])
print(s.searchRange([], 0), [-1,-1])