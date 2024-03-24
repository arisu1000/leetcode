from typing import List

class Solution:
    def getPermutation(self, nums: List[int]):
        
        def backtrack(startIndex):
            if startIndex == len(nums) - 1:
                result.append(nums[:])
            else:
                for i in range(startIndex, len(nums)):
                    nums[startIndex], nums[i] = nums[i], nums[startIndex]
                    backtrack(startIndex + 1)
                    
                    nums[startIndex], nums[i] = nums[i], nums[startIndex]
                    
        
        result = []
        backtrack(0)
        return result

s = Solution()

print(s.getPermutation([1,2,3]))
