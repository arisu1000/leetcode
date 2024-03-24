from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        spiral = []

        while row_start <= row_end and col_start <= col_end:
            # Traverse top row
            for col in range(col_start, col_end + 1):
                spiral.append(matrix[row_start][col])
            row_start += 1

            # Traverse right column
            for row in range(row_start, row_end + 1):
                spiral.append(matrix[row][col_end])
            col_end -= 1

            if row_start <= row_end:
                # Traverse bottom row
                for col in range(col_end, col_start - 1, -1):
                    spiral.append(matrix[row_end][col])
                row_end -= 1

            if col_start <= col_end:
                # Traverse left column
                for row in range(row_end, row_start - 1, -1):
                    spiral.append(matrix[row][col_start])
                col_start += 1

        return spiral
    
s = Solution()

# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
