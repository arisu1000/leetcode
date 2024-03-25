#https://leetcode.com/problems/merge-sorted-array/description/

import itertools
import math
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m+n
        result = [0 for i in range(length)]
        
        cursor = 0
        nums1_cursor = 0
        nums2_cursor = 0
        while cursor < length:
            if nums1_cursor < m and nums2_cursor < n:
                if nums1[nums1_cursor] <= nums2[nums2_cursor]:
                    result[cursor] = nums1[nums1_cursor]
                    nums1_cursor += 1
                else:
                    result[cursor] = nums2[nums2_cursor]
                    nums2_cursor += 1
            else:
                if nums1_cursor >= m:
                    result[cursor] = nums2[nums2_cursor]
                    nums2_cursor +=1
                elif nums2_cursor >= n:
                    result[cursor] = nums1[nums1_cursor]
                    nums1_cursor += 1

            cursor += 1

        for i in range(length):
            nums1[i] = result[i]

        print(nums1)


        
s = Solution()

print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))
print(s.merge([2,0], 1, [1], 1))