# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        result = 0
        for c in s:
            if c == '1':
                result += 1
        return result



s = Solution()
print(s.hammingWeight(11), 3)
print(s.hammingWeight(128), 1)
print(s.hammingWeight(2147483645), 30)