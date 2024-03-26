https://leetcode.com/problems/remove-element

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []

        for n in nums:
            if n != val:
                result.append(n)

        for i in range(len(nums)):
            if i < len(result):
                nums[i] = result[i]

        del nums[len(result):]

        nums = result

s = Solution()

print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))