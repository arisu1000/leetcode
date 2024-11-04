# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:].zfill(32)

        s = s[::-1]

        return int(s, 2)
    
s = Solution()
print(s.reverseBits(43261596), 964176192 )
print(s.reverseBits(4294967293), 3221225471 )
