# https://leetcode.com/problems/kth-largest-element-in-an-array

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
s = Solution()

print(s.findKthLargest([3,2,1,5,6,4], 2), 5)
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)