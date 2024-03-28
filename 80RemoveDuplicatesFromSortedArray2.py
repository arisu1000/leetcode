#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        countTwo = 0
        while i < len(nums) - 1:

            if nums[i] == nums[i+1]:
                countTwo += 1
                if countTwo >= 2:
                    nums.pop(i)
                else:
                    i += 1 
            else:
                countTwo = 0
                i += 1        

        return len(nums)

s = Solution()

print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))