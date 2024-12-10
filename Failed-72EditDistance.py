# https://leetcode.com/problems/edit-distance/description

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # 초기값 설정
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # DP 테이블 채우기
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    cost = 0
                else:
                    cost = 1

                dp[i][j] = min(dp[i-1][j] + 1, #삭제
                                dp[i][j-1] + 1, #삽입
                                dp[i - 1][j - 1] + cost) #교체
                
        return dp[m][n]


s = Solution()
print(s.minDistance("horse", "ros"), 3)
print(s.minDistance("intention", "execution"), 5)