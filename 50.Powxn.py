class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        n_is_minus = False
        if n < 0:
            n = n * - 1
            x = 1/x
        
        for i in range(n):
            result = result*x

        return result

        # if n == 0:
        #     return 1
        
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        
        # half = self.myPow(x, n // 2)
        
        # if n % 2 == 0:
        #     return half * half
        # else:
        #     return half * half * x        

s = Solution()
print(s.myPow(2.00000, 10))
print(s.myPow(2.10000, 3))
print(s.myPow(2.00000, -2))
# print(s.myPow(0.00001, 2147483647))
