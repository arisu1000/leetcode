
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        nums.sort()
        result = []
        for i in range(0, len_nums):
            for j in range(len_nums - 1, i + 2, -1):
                k = i + 1
                t = j - 1
                while k < t:
                    tmp_sum = nums[i] + nums[k] + nums[t] + nums[j]
                    if target == tmp_sum:
                        check_equal_member = False
                        for r in result:
                            if r == [nums[i], nums[k], nums[t], nums[j]]:
                                check_equal_member = True
                        if check_equal_member == False:
                            result.append([nums[i], nums[k], nums[t], nums[j]])
                        k += 1
                        t -=1
                    elif target > tmp_sum:
                        k += 1
                    elif target < tmp_sum:
                        t -= 1

        return result

s = Solution()

print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))
print(s.fourSum([-3,-1,0,2,4,5], 0))
print(s.fourSum([1,0,-1,0,-2,2], 0))