# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift        


s = Solution()

print(s.rangeBitwiseAnd(5, 7), 4)
print(s.rangeBitwiseAnd(0, 0), 0)
print(s.rangeBitwiseAnd(1, 2147483647), 0)