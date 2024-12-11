# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # 거래 횟수가 충분히 큰 경우(사실상 제한 없음)
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            
            return max_profit
        
        # DP 테이블 초기화
        dp = [[0] * n for _ in range(k+1)]

        for i in range(1, k+1):
            max_diff = - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[k][n-1]

    
s = Solution()
print(s.maxProfit(2, [2,4,1]), 2)
print(s.maxProfit(2, [3,2,6,5,0,3]), 7)