class Solution:
    def myAtoi(self, s: str) -> int:
        parsingStr = ""

        for c in s:
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                parsingStr = parsingStr + c
            elif c in ['-', '+']:
                if len(parsingStr) == 0:
                    parsingStr = c
                else:
                    break
            elif c == ' ' and len(parsingStr) == 0:
                continue
            elif c == '.':
                if len(parsingStr) == 0:
                    return 0
                break
            else:
                if len(parsingStr) == 0:
                    return 0
                else:
                    break

        if len(parsingStr) == 0:
            return 0

        try:
            num_str = int(parsingStr)
            if num_str < -2**31:
                return -2**31
            elif num_str > 2**31 -1:
                return 2**31 -1
            else:
                return num_str 
        except:
            return 0

s = Solution()

print(s.myAtoi("42"))
print(s.myAtoi("    -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("3.14159"))
print(s.myAtoi(".1"))
print(s.myAtoi("+-12"))
print(s.myAtoi(""))
print(s.myAtoi("  -0012a42"))
print(s.myAtoi("-5-"))