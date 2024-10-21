# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        minVal = nums[0]

        for n in nums:
            minVal = min(minVal, n)        

        return minVal

s = Solution()
print(s.findMin([3,4,5,1,2]), 1)
print(s.findMin([4,5,6,7,0,1,2]), 0)
print(s.findMin([11,13,15,17]), 11)