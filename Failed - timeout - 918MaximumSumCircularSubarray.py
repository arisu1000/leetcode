#https://leetcode.com/problems/maximum-sum-circular-subarray

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_max = -100000
        for start_index in range(len(nums)):
            current_index = start_index
            max_sum = current_sum = nums[current_index]

            current_index += 1
            if current_index == len(nums):
                    current_index -= len(nums)
            
            while current_index != start_index:
                current_sum = max(current_sum + nums[current_index], nums[current_index])
                max_sum = max(max_sum, current_sum)

                current_index += 1
                if current_index == len(nums):
                    current_index -= len(nums)
            
            total_max = max(total_max, max_sum)
        
        return total_max
        


s = Solution()

print(s.maxSubarraySumCircular([1,-2,3,-2]), 3)
print(s.maxSubarraySumCircular([5,-3,5]), 10)
print(s.maxSubarraySumCircular([-3,-2,-3]), -2)


