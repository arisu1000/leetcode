# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n

        return count

s = Solution()


print(s.trailingZeroes(30), 7)
print(s.trailingZeroes(10), 2)
print(s.trailingZeroes(6), 1)
print(s.trailingZeroes(3), 0)
print(s.trailingZeroes(5), 1)
print(s.trailingZeroes(0), 0)
print(s.trailingZeroes(1574), 0)