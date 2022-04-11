class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_len = len(x_str)
        for i in range(0, x_len):
            if x_str[i] != x_str[(x_len - 1) - i]:
                return False
        return True

s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
