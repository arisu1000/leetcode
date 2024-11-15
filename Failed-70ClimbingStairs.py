# https://leetcode.com/problems/climbing-stairs

class Solution:
    result = 0
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        #초기값 설정
        first, second = 1, 2
        for i in range(3, n+1):
            # 현재 계단의 방법 수 계산
            current = first + second
            # 값 갱신
            first, second = second, current

        return second
    
s = Solution()

print(s.climbStairs(2), 2)
print(s.climbStairs(3), 3)
print(s.climbStairs(4), 5)
print(s.climbStairs(5), 8)
print(s.climbStairs(38), 63245986)
