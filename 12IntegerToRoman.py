#https://leetcode.com/problems/integer-to-roman

import math

class Solution:
    def intToRoman(self, num: int) -> str:
        dic1 = {"0":"", "1":"I", "2": "II", "3": "III", "4": "IV", "5": "V", "6":"VI", "7": "VII", "8": "VIII", "9": "IX"}
        dic10 = {"0":"", "1":"X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6":"LX", "7": "LXX", "8": "LXXX", "9": "XC"}
        dic100 = {"0":"", "1":"C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6":"DC", "7": "DCC", "8": "DCCC", "9": "CM"}
        dic1000 = {"0":"", "1":"M", "2": "MM", "3": "MMM"}

        result = ""
        str_num = str(num)
        length = len(str_num)
        for i in range(length):
            if i == 0:
                result = dic1[str_num[length - 1 - i]] + result
            elif i == 1:
                result = dic10[str_num[length - 1 - i]] + result
            elif i == 2:
                result = dic100[str_num[length - 1 - i]] + result
            elif i == 3:
                result = dic1000[str_num[length - 1 - i]] + result

        return result


s = Solution()

print(s.intToRoman(3), "III")
print(s.intToRoman(58), "LVIII")
print(s.intToRoman(1994), "MCMXCIV")
print(s.intToRoman(10), "X")
