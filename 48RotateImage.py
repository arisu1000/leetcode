from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        
        result = [[0 for j in range(n)] for i in range(n)]
        for x in range(n):
            for y in range(n):
                result[y][(n-1)-x] = matrix[x][y]
        
        for i in range(n):
            matrix[i] = result[i][:]
        print(matrix)
        
    

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])