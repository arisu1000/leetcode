# https://leetcode.com/problems/find-peak-element

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        len_nums = len(nums)

        if len_nums == 1:
            return 0

        for i in range(len_nums-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
        
        if nums[len_nums-1] > nums[len_nums-2]:
            return len(nums) - 1



    

s = Solution()

print(s.findPeakElement([2, 1]), 0)
print(s.findPeakElement([1,2,3,1]), 2)
print(s.findPeakElement([1,2,1,3,5,6,4]), 5)