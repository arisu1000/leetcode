# https://leetcode.com/problems/search-insert-position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i] :
                return i
        
        return len(nums)


    


s = Solution()

print(s.searchInsert([1,3,5,6], 5), 2)
print(s.searchInsert([1,3,5,6], 2), 1)
print(s.searchInsert([1,3,5,6], 7), 4)