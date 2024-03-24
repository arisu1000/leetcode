from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        
        # if n == 1:
        #     return True

        # target_index = n - 1

        # def find(index) -> bool:
        #     for i in range(1, nums[index]+1):
        #         nextIndex = i + index
        #         if nextIndex == target_index:
        #             return True
        #         elif nextIndex > target_index:
        #             return False
        #         else:
        #             if find(nextIndex):
        #                 return True

        # if find(0):
        #     return True

        # return False


        last_pos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # print(i, nums[i], last_pos)
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))