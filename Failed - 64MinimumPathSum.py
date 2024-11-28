# https://leetcode.com/problems/minimum-path-sum

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # 첫 번째 행 채우기
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # 첫 번째 열 채우기
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # 나머지 셀 채우기
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j-1])

        return dp[m-1][n-1]
    
s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
print(s.minPathSum([[1,2,3],[4,5,6]]), 12)
print(s.minPathSum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]), 47)