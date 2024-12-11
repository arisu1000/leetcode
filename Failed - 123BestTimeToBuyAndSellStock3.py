# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # 최대 두 번의 거래를 처리하기 위해 필요한 변수 정의
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for price in prices:
            # 첫번째 주식을 구매
            first_buy = max(first_buy, - price)
            # 첫번째 주식을 구매
            first_sell = max(first_sell, first_buy+price)
            # 두번째 주식을 구매
            second_buy = max(second_buy, first_sell - price)
            # 두 번째 주식을 판매
            second_sell = max(second_sell, second_buy + price)

        return second_sell



s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]), 6)
print(s.maxProfit([1,2,3,4,5]), 4)
print(s.maxProfit([7,6,4,3,1]), 0)
