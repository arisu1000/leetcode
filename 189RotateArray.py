#https://leetcode.com/problems/rotate-array

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        lastIndex = len(nums) - 1
        while i < k:
            n = nums.pop(lastIndex)
            nums.insert(0, n)
            i += 1

        
s = Solution()

nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)