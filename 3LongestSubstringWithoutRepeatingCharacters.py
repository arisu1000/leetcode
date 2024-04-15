#https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        substring = ""

        i = 0
        len_s = len(s)
        while i < len_s:
            for c in range(len(substring)):
                if substring[c] == s[i]:
                    ans = max(ans, len(substring))
                    i = (i - len(substring))+1
                    substring=""
                    break
            
            substring += s[i]
            i += 1

        return max(ans, len(substring))
        

s = Solution()
print(s.lengthOfLongestSubstring("dvdf"), 3)
print(s.lengthOfLongestSubstring(" "), 1)
print(s.lengthOfLongestSubstring("cdd"), 2)
print(s.lengthOfLongestSubstring("abcabcbb"), 3)
print(s.lengthOfLongestSubstring("bbbbb"), 1)
print(s.lengthOfLongestSubstring("pwwkew"), 3)