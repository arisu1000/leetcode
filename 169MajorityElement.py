#https://leetcode.com/problems/majority-element/description

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            try:
                count[n] += 1
            except KeyError:
                count[n] = 1
            
        max = list(count.keys())[0]
        for key in count:
            if count[key] > count[max]:
                max = key
        
        return max


s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))