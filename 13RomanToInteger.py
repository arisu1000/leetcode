#https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        i = 0

        result = 0
        previous_str = ""
        while i<length:
            if s[i] == "I":
                result += 1
                previous_str = "I"
            elif s[i] == "V":
                result += 5
                if previous_str == "I":
                    result -= 2
                previous_str = "V"
            elif s[i] == "X":
                result += 10
                if previous_str == "I":
                    result -= 2
                previous_str = "X"
            elif s[i] == "L":
                result +=50
                if previous_str == "X":
                    result -=20
                previous_str = "L"
            elif s[i] == "C":
                result += 100
                if previous_str == "X":
                    result -= 20
                previous_str = "C"
            elif s[i] == "D":
                result += 500
                if previous_str == "C":
                    result -= 200
                previous_str = "D"
            elif s[i] == "M":
                result += 1000
                if previous_str == "C":
                    result -= 200
                previous_str = "M"
            
            i += 1

        return result 

s = Solution()

print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))