from typing import List

#문제 내용을 이해 못했음.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        current = 0
        long = 0
        count = 0
        for i in range(n - 1):
            long =  max(i + nums[i], long)
            if i == current:
                current = long
                count += 1

        return count

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([0]))
