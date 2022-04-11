from distutils.command.build_scripts import first_line_re

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        laststr = ""
        tmpstr = ""
       
        uncount = 0
        for i, w in enumerate(s):
            if i == 0:
                laststr = w
                tmpstr = w
            
            equalStr = False
            tmpstrstartindex = 0
            for j, ls in enumerate(tmpstr):
                if ls == s[i]:
                    equalStr = True
                    tmpstrstartindex = j + 1
                    break

            if equalStr == False:
                tmpstr = f"{tmpstr}{s[i]}"
            else:
                tmpstr = f"{tmpstr[tmpstrstartindex:]}{s[i]}" 

            if len(laststr) <= len(tmpstr):
                laststr = tmpstr

        print(tmpstr, laststr)
        return len(laststr)

s= Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring("kdgjkjhglfp"))
print(s.lengthOfLongestSubstring("ggububgvfk"))
