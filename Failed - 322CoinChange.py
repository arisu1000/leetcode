# https://leetcode.com/problems/coin-change

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp 배열 초기화
        dp = [amount+1] * (amount +1)
        dp[0] = 0 # 0원을 만드는 데 필요한 동전 수는 0개

        # dp 배열 채우기
        for coin in coins:
            for i in range(coin, amount +1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        # 결과 반환
        return dp[amount] if dp[amount] != amount + 1 else -1



s = Solution()


print(s.coinChange([186,419,83,408], 6249), 20)
print(s.coinChange([1], 2), 2)
print(s.coinChange([1,2,5], 11), 3)
print(s.coinChange([2], 3), -1)
print(s.coinChange([1], 0), 0)