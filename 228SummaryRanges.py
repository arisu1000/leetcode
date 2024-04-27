#https://leetcode.com/problems/summary-ranges

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = 0

        if len(nums) == 0:
            return ans
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                if nums[start] == nums[i]:
                    ans.append("{end}".format(end=nums[i]))
                else:
                    ans.append("{start}->{end}".format(start=nums[start],end=nums[i]))
                start = i+1

        if start == len(nums) - 1:
            ans.append("{end}".format(end=nums[start]))
        else:
            ans.append("{start}->{end}".format(start=nums[start],end=nums[len(nums)-1]))

        return ans
            


            


s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
print(s.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])