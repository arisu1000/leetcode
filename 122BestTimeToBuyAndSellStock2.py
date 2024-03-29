#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#TODO: can improve speed

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        i = 0

        TotalProfit = 0
        while i<length:
            j = i
            
            maxProfit = 0
            maxIndex = j
            isNew = False
            while j < length:
                if prices[i] > prices[j]:
                    break

                if isNew == True and prices[j] < prices[maxIndex] and prices[j] >= prices[i]:
                    break
            
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    isNew = True
                    maxProfit = profit
                    maxIndex = j

                j += 1

            if isNew:
                TotalProfit += maxProfit
                i = maxIndex
            else:
                i += 1        
            
        
        return TotalProfit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,6,8,7,8,7,9,4,1,2,4,5,8]))