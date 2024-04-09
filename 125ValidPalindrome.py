#https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ""
        for c in s:
            if c.isalnum():
                chars += c
        chars = chars.lower()
        left = 0
        right = len(chars) - 1
        while left < right:
            if chars[left] == chars[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"), True)
print(s.isPalindrome("race a car"), False)
print(s.isPalindrome(" "), True)
print(s.isPalindrome("0P"), False)
print(s.isPalindrome("a"), True)
