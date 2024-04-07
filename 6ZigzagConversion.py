#https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        len_s = len(s)
        rows = [""]*numRows

        count = 0
        rowIndex = 0
        down = True
        while count < len_s:
            rows[rowIndex] += s[count]
            if down:
                rowIndex += 1
                if rowIndex == numRows -1:
                    down=False
                
            else:
                rowIndex -= 1
                if rowIndex == 0:
                    down=True
                
            count += 1

        result = ""
        for r in rows:
            result += r

        return result

s = Solution()


print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))
print(s.convert("AB", 1))
