from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def findAll(nums, subResult, result):

            if len(subResult) == len(nums) :
                if subResult[:] not in result:
                    result.append(subResult[:])

                return

            for num in nums:
                subResult.append(num)
                findAll(nums, subResult, result)
                subResult.pop()

        findAll(nums, [], result)
        
        return result


s = Solution()
print(s.permuteUnique([1,1,2]))

