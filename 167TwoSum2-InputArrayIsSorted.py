# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex = 0
        rightIndex = len(numbers) - 1

        while True:
            sum = numbers[leftIndex] + numbers[rightIndex]
            if sum < target:
                leftIndex += 1
            elif sum > target:
                rightIndex -= 1
            else:
                break

        return [leftIndex + 1, rightIndex + 1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9), [1, 2])
print(s.twoSum([2, 3, 4], 6), [1, 3])
print(s.twoSum([-1, 0], -1), [1, 2])
