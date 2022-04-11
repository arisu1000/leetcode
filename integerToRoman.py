import math

class Solution:
    def intToRoman(self, num: int) -> str:
        # m_num = math.floor(num / 1000)
        # d_num = math.floor(num / 1000)
        # c_num = math.floor(num / 1000)
        # l_num = math.floor(num / 1000)
        # x_num = math.floor(num / 1000)
        # v_num = math.floor(num / 1000)
        # i_num = math.floor(num / 1000)
        
        num_str = str(num)
        len_str = len(num_str)
        result_str = ""
        for i in range(0, len_str):
            if len_str - i == 1:
                if num_str[i] == "1":
                    result_str = result_str + "I"
                elif num_str[i] == "2":
                    result_str = result_str + "II"
                elif num_str[i] == "3":
                    result_str = result_str + "III"
                elif num_str[i] == "4":
                    result_str = result_str + "IV"
                elif num_str[i] == "5":
                    result_str = result_str + "V"
                elif num_str[i] == "6":
                    result_str = result_str + "VI"
                elif num_str[i] == "7":
                    result_str = result_str + "VII"
                elif num_str[i] == "8":
                    result_str = result_str + "VIII"
                elif num_str[i] == "9":
                    result_str = result_str + "IX"
            elif len_str - i == 2:
                if num_str[i] == "1":
                    result_str = result_str + "X"
                elif num_str[i] == "2":
                    result_str = result_str + "XX"
                elif num_str[i] == "3":
                    result_str = result_str + "XXX"
                elif num_str[i] == "4":
                    result_str = result_str + "XL"
                elif num_str[i] == "5":
                    result_str = result_str + "L"
                elif num_str[i] == "6":
                    result_str = result_str + "LX"
                elif num_str[i] == "7":
                    result_str = result_str + "LXX"
                elif num_str[i] == "8":
                    result_str = result_str + "LXXX"
                elif num_str[i] == "9":
                    result_str = result_str + "XC"
            elif len_str - i == 3:
                if num_str[i] == "1":
                    result_str = result_str + "C"
                elif num_str[i] == "2":
                    result_str = result_str + "CC"
                elif num_str[i] == "3":
                    result_str = result_str + "CCC"
                elif num_str[i] == "4":
                    result_str = result_str + "CD"
                elif num_str[i] == "5":
                    result_str = result_str + "D"
                elif num_str[i] == "6":
                    result_str = result_str + "DC"
                elif num_str[i] == "7":
                    result_str = result_str + "DCC"
                elif num_str[i] == "8":
                    result_str = result_str + "DCCC"
                elif num_str[i] == "9":
                    result_str = result_str + "CM"
            elif len_str - i == 4:
                if num_str[i] == "1":
                    result_str = result_str + "M"
                elif num_str[i] == "2":
                    result_str = result_str + "MM"
                elif num_str[i] == "3":
                    result_str = result_str + "MMM"

        return result_str


s = Solution()

print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
