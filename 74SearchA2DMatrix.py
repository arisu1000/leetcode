# https://leetcode.com/problems/search-a-2d-matrix

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == target:
                    return True
                
                if matrix[r][c] > target:
                    return False
                else:
                    c += 1

        return False
    
s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix, 3), True)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix, 13), False)
