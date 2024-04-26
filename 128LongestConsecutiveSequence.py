#https://leetcode.com/problems/longest-consecutive-sequence

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(set(nums))
        start=0
        end=0
        longest = 0
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                end = i+1
            else:
               end=i
               longest = max(longest, (end-start) + 1)
               start = i+1

        longest = max(longest, (end - start) + 1)
        
        return longest

               



s = Solution()
print(s.longestConsecutive([]), 0)
print(s.longestConsecutive([1,2,0,1]), 3)
print(s.longestConsecutive([100,4,200,1,3,2]), 4)
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)