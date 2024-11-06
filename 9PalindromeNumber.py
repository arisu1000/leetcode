# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        len_s = len(s)
        left = 0
        right = len_s - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
    
s = Solution()

print(s.isPalindrome(121), True)
print(s.isPalindrome(-121), False)
print(s.isPalindrome(10), False)