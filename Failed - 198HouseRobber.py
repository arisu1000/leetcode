# https://leetcode.com/problems/house-robber

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        n = len(nums)

        #집의 수가 1개 또는 2개인 경우 특별 처리
        if n == 1:
            return nums[0]
    
        # dp[i]는 첫 번째 집부터 i번째 집까지의 최대 도둑질 금액을 저장합니다.
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # dp 배열을 채워나갑니다.
        for i in range(2, n):
            # 현재 집을 털지 않거나, 현재 집을 털고 두 칸 전의 금액을 더합니다.
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # 마지막 요소가 최종 결과입니다.

        return dp[-1]
    
s = Solution()

print(s.rob([1,2,3,1]), 4)
print(s.rob([2,7,9,3,1]), 12)