#https://leetcode.com/problems/set-matrix-zeroes

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        len_m = len(matrix)
        if len_m > 0:
            len_n = len(matrix[0])
        
        check_m = set()
        check_n = set()
        for m in range(len_m):
            for n in range(len_n):
                if matrix[m][n] == 0:
                    check_m.add(m)
                    check_n.add(n)

        for m in check_m:
            for n in range(len_n):
                matrix[m][n] = 0
        for n in check_n:
            for m in range(len_m):
                matrix[m][n] = 0

        

s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix, [[1,0,1],[0,0,0],[1,0,1]])
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
