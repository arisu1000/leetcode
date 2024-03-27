#https://leetcode.com/problems/remove-duplicates-from-sorted-array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        removed = 0
        i = 0
        while i < len(nums) - 1:

            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                removed += 1
            else:
                i += 1

        return length - removed

        
s = Solution()


print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))