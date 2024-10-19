#https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        direction = 'toRight'
        if nums[0] > target:
            start_index = len(nums) - 1
            direction = 'toLeft'

        if direction == 'toRight':
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1
        else:
            for i in range(len(nums)-1,0,-1):
                if nums[i] == target:
                    return i
                elif nums[i] < target:
                    return -1

        return -1
    

s = Solution()

print(s.search([1,3], 3), 1)
print(s.search([4,5,6,7,0,1,2], 0), 4)
print(s.search([4,5,6,7,0,1,2], 3), -1)
print(s.search([1], 0), -1)