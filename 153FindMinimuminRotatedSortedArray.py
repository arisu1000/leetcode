# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid

        return nums[left]

s = Solution()
print(s.findMin([5,1,2,3,4]), 1)
print(s.findMin([2,1]), 1)
print(s.findMin([3,4,5,1,2]), 1)
print(s.findMin([4,5,6,7,0,1,2]), 0)
print(s.findMin([11,13,15,17]), 11)