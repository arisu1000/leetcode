# https://leetcode.com/problems/median-of-two-sorted-arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        new_list = []
        total_n = len(nums1) + len(nums2)

        i, j = 0, 0
        while len(new_list) < total_n:

            if i == len(nums1):
              new_list.append(nums2[j])
              j += 1  
            elif j == len(nums2):
                new_list.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
            
        if total_n % 2 == 0:
            return (new_list[(total_n // 2) - 1] + new_list[total_n // 2])/2
        else:
            return new_list[total_n // 2]
            


    

s = Solution()

print(s.findMedianSortedArrays([1,3], [2]), 2.0000)
print(s.findMedianSortedArrays([1,2], [3,4]), 2.5000)