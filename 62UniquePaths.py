import itertools
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return math.factorial(m-1 + n-1)/(math.factorial(m-1)*math.factorial(n-1))
            
        
        

s = Solution()
print(s.uniquePaths(3,2))
print(s.uniquePaths(3,7))

