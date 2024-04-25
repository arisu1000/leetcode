#https://leetcode.com/problems/two-sum

from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            value = target -  nums[i]
            if value in nums:
                for j in range(len(nums) - 1, i , -1):
                    if nums[j] == value:
                        return [i,j]


s = Solution()
print(s.twoSum([2,7,11,15], 9), [0,1])
print(s.twoSum([3,2,4], 6), [1,2])
print(s.twoSum([3,3], 6), [0, 1])

