from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        print(m, n)
        

        return 0
    
s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))