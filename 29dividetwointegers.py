class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        max = pow(2, 31) -1
        min = pow(-2, 31)
        result = 0

        is_minus = False
        if dividend < 0:
            dividend = -dividend
            is_minus = not is_minus
        if divisor < 0:
            divisor = -divisor
            is_minus = not is_minus

        while dividend >= divisor:
            count = 1
            tmp_divisor = divisor
            while tmp_divisor + tmp_divisor <= dividend:
                tmp_divisor += tmp_divisor
                count += count
            
            dividend -= tmp_divisor
            result += count

        if is_minus:
            result = -result

        if result >= max:
            return max
        if result <= min:
            return min

        return result 

s = Solution()


print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(-2147483648, -1))
print(s.divide(1, 2))