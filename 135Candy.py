#https://leetcode.com/problems/candy

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        length = len(ratings)
        candys = [1] * length
        i = 0
        while i < length:
            left = i - 1
            right = i + 1

            isAdd = False
            tmpList = []
            if left > -1 and ratings[left] < ratings[i]:
                isAdd = True
                tmpList.append(candys[left])
            
            if right < length and ratings[i] > ratings[right]:
                isAdd = True
                tmpList.append(candys[right])

            if isAdd:
                candys[i] = max(tmpList) + 1

            i += 1

        i=length - 1
        while i > -1:
            left = i - 1
            right = i + 1

            isAdd = False
            tmpList = []
            if left > -1 and ratings[left] < ratings[i]:
                isAdd = True
                tmpList.append(candys[left])
            
            if right < length and ratings[i] > ratings[right]:
                isAdd = True
                tmpList.append(candys[right])

            if isAdd:
                candys[i] = max(tmpList) + 1

            i -= 1

        return sum(candys)
        

s = Solution()
print(s.candy([1,0,2]), 5)
print(s.candy([1,2,2]), 4)
print(s.candy([1]), 1)
print(s.candy([1,2,87,87,87,2,1]), 13)