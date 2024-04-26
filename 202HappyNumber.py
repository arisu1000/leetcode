#https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:        
        memo = []
        while n != 1:
            n = self.checkHappy(n)
            if n in memo:
                return False
            memo.append(n)
        
        return True

    def checkHappy(self, n: int) -> int:
        str_n = str(n)
        sum = 0
        for s in str_n:
            sum += pow(int(s), 2)
        return sum



s = Solution()
print(s.isHappy(19), True)
print(s.isHappy(2), False)