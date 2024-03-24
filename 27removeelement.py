from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        count_remove = 0
        for i in range(0, len_nums):
            if val == nums[i - count_remove]:
                nums.pop(i - count_remove)
                count_remove += 1

        return len_nums - count_remove

s = Solution()

print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))