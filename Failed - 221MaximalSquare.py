# https://leetcode.com/problems/maximal-square

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: # 첫 행이나 첫 열에서는 그대로 1
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j]) # 가장 큰 변 업데이트

                        

        return max_side * max_side
    

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

s = Solution()
print(s.maximalSquare(matrix), 4)


matrix = [["0","1"],
          ["1","0"]]
print(s.maximalSquare(matrix), 1)

matrix =[["0"]]
print(s.maximalSquare(matrix), 0)