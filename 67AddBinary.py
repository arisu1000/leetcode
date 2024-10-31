# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_a = int(a, 2)
        b_b = int(b, 2)

        result = b_a + b_b

        return bin(result)[2:]
    
s = Solution()

print(s.addBinary('11', '1'), '100')
print(s.addBinary('1010', '1011'), '10101')
