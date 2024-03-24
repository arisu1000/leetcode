from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []


        def findAll(nums, subResult, result):

            if len(subResult) == len(nums):
                result.append(subResult[:])
                return

            for num in nums:
                if num not in subResult:
                    subResult.append(num)
                    findAll(nums, subResult, result)
                    subResult.pop()

        findAll(nums, [], result)
        
        return result


s = Solution()
print(s.permute([1,2,3,4]))

