#https://leetcode.com/problems/trapping-rain-water

#TODO: 실패
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftIndex = 0
        rightIndex = 0

        totalResult = 0
        tempResult = 0
        while rightIndex < length and leftIndex < length:
          if height[leftIndex] > height[rightIndex]:
             tempResult = tempResult + (height[leftIndex] - height[rightIndex])
             rightIndex += 1
          else:
             totalResult += tempResult
             tempResult = 0
             leftIndex = rightIndex
             rightIndex += 1
          
          # if rightIndex == length - 1 and height[leftIndex] > height[rightIndex]:
          #    leftIndex += 1
          #    rightIndex = leftIndex + 1
          #    tempResult = 0

        if height[0] != height[length - 1]:

          tempResult = 0
          leftIndex = length - 1
          rightIndex = length - 1
          while leftIndex > -1 and rightIndex > -1:
            if height[rightIndex] > height[leftIndex]:
              tempResult = tempResult + (height[rightIndex] - height[leftIndex])
              leftIndex -= 1
            else:
              totalResult += tempResult
              tempResult = 0
              rightIndex = leftIndex
              leftIndex -= 1

        return totalResult


s = Solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
# print(s.trap([4,2,0,3,2,5]), 9)
# print(s.trap([4,2,3]), 1)
print(s.trap([5,5,1,7,1,1,5,2,7,6]), 23)