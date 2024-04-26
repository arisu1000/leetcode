#https://leetcode.com/problems/contains-duplicate-ii

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:min(len(nums), i+1+k)]:
                return True
        
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3), True)
print(s.containsNearbyDuplicate([1,0,1,1], 1), True)
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2), False)