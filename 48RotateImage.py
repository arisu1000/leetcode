#https://leetcode.com/problems/rotate-image

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_len = len(matrix)

        result = [[999] * matrix_len for _ in range(matrix_len)]
        
        for i in range(matrix_len):
            for j in range(matrix_len):
                result[j][matrix_len - 1 - i] = matrix[i][j]

        for i in range(matrix_len):
            matrix[i] = result[i]        

        return None


s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
print(matrix, [[7,4,1],[8,5,2],[9,6,3]])

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])