# https://leetcode.com/problems/triangle

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # 삼각형의 마지막 행에서 시작
        dp = triangle[-1]

        # 마지막 전 행부터 시작하여 위로 올라감
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # 현재 위치의 값 + 다음 행의 가능한 최소 값
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        # 최상단의 최소 경로 합

        return dp[0]


s = Solution()
print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]), -1)
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
print(s.minimumTotal([[-10]]), -10)
