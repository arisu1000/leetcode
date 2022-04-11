from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_nums = nums1 + nums2
        merge_nums.sort()
        # print(merge_nums)
        mergelength = len(merge_nums)
        medianindex = math.floor(mergelength/2)
        if mergelength % 2 == 1:
            # print(merge_nums[medianindex])
            return merge_nums[medianindex]
        else:
            # print((merge_nums[medianindex] + merge_nums[medianindex - 1])/2)
            return (merge_nums[medianindex] + merge_nums[medianindex - 1])/2


s = Solution()

s.findMedianSortedArrays([1,3], [2]) 
s.findMedianSortedArrays([1,2], [3, 4]) 
