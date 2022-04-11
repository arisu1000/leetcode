class Solution:
    def reverse(self, x: int) -> int:
        
        x_str = str(x)
        x_str_reverse = x_str[::-1]
        if x_str[0] == "-":
            x_str_reverse = "-" + x_str_reverse[:len(x_str_reverse)-1]      

        reverse_x_int = int(x_str_reverse)
        if reverse_x_int < -2**31 or reverse_x_int > 2**31 -1:
            return 0

        return reverse_x_int 

s = Solution()

print(2**31 -1)

print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(1534236469))