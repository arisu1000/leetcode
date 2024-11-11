# https://leetcode.com/problems/powx-n

import math

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # n이 음수일 경우 x의 역수를 취하고 n을 양수로 바꿈
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x

        while n > 0:
            # n이 홀수일 때 현재 결과에 current_product를 곱함
            if n % 2 == 1:
                result *= current_product
            
            # current_product를 제곱하고, n을 절반으로 줄임
            current_product *= current_product
            n //= 2

        return result



s = Solution()
print(s.myPow(2.00000, 10), 1024)
print(s.myPow(2.10000, 3), 9.26100)
print(s.myPow(2.00000, -2), 0.25)
print(s.myPow(0.00001, 2147483647), 0)
