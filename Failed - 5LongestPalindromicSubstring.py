# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 0:
            return ""        

        # DP 테이블 초기화
        dp = [[False] *n for _ in range(n)]

        # 가장 긴 팰린드롬 부분 문자열의 시작과 길이
        start = 0
        max_length = 1

        # 길이 1 부분 문자열은 항상 팰린드롬
        for i in range(n):
            dp[i][i] = True
        
        # 길이 2 부분 문자열 초기화
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2

        # 길이 3 이상 부분 문자열 검사
        for length in range(3, n+1): # length는 부분 문자열의 길이
            for i in range(n - length + 1):
                j = i + length -1 # 부분 문자열의 끝 인덱스
                if s[i] == s[j] and dp[i + 1][j - 1]: # 양 끝이 같고 안쪽이 팰린드롬이면
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        # 가장 긴 팰린드롬 부분 문자열 반환
        return s[start:start + max_length]


s = Solution()
print(s.longestPalindrome("babad"), "bab")
print(s.longestPalindrome("cbbd"), "bb")