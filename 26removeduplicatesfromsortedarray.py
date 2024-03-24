from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_num = len(nums)
        prev = -1000
        count_remove = 0
        for i in range(0, len_num):    
            if prev == nums[i - count_remove]:
                nums.pop(i - count_remove)
                count_remove += 1
            else:
                prev = nums[i - count_remove]
        return len_num - count_remove

s = Solution()


print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))