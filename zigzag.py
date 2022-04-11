class Solution:
    def convert(self, s: str, numRows: int) -> str:
      
      if numRows == 1:
          return s

      matrix = {}
      targetNum = numRows + (numRows - 2)

      for i in range(numRows):
          matrix[i] = []

      ToDown = True
      rowIndex = 0
      for c in s:
          matrix[rowIndex].append(c)
          if ToDown:
              rowIndex = rowIndex + 1
              if rowIndex == numRows -1:
                  ToDown = False
          else:
              rowIndex = rowIndex - 1
              if rowIndex == 0:
                ToDown = True

      result = ""
      for i in range(numRows):
          result = result + ''.join(matrix[i])

      return result

s = Solution()


# print(s.convert("PAYPALISHIRING", 3))
# print(s.convert("PAYPALISHIRING", 4))
print(s.convert("AB", 1))
