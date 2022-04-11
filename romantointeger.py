class Solution:
    def romanToInt(self, s: str) -> int:

        s_len = len(s)
        result = 0
        skip_index = False
        for i in range(0, s_len):
            if skip_index == True:
                skip_index = False
                continue

            if s[i] == "M":
                result += 1000
            elif s[i] == "D":
                result += 500
            elif s[i] == "C":
                if i+1 < s_len and s[i+1] == "D":
                    result += 400
                    skip_index = True
                elif i+1 < s_len and s[i+1] == "M":
                    skip_index = True
                    result += 900
                else:
                    result += 100
            elif s[i] == "L":
                result += 50
            elif s[i] == "X":
                if i+1 < s_len and s[i+1] == "L":
                    skip_index = True
                    result += 40
                elif i+1 < s_len and s[i+1] == "C":
                    skip_index = True
                    result += 90
                else:    
                    result += 10
            elif s[i] == "V":
                result += 5
            elif s[i] == "I":    
                if i+1 < s_len and s[i+1] == "V":
                    skip_index = True
                    result += 4
                elif i+1 < s_len and s[i+1] == "X":
                    skip_index = True
                    result += 9
                else:    
                    result += 1
            
        return result

s = Solution()

print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))