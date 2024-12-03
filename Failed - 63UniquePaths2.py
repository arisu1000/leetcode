# https://leetcode.com/problems/unique-paths-ii

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 시작점이나 끝점이 장애물이면 경로가 없음
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # DP 배열 초기화
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 # 시작점
        
        # 첫 번째 행 초기화
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

        # 첫 번째 열 초기화
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

        # DP 테이블 채우기
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0: # 장애물이 없을 때만 계산
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        


s = Solution()

print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)
print(s.uniquePathsWithObstacles([[0,1],[0,0]]), 1)

