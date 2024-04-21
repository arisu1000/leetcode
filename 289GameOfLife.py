#https://leetcode.com/problems/game-of-life

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        len_board = len(board)
        len_row = len(board[0])

        ans = [ [0] * len_row for _ in range(len_board) ]
        for i in range(len_board):
            for j in range(len_row):
                neighbors = 0
                
                if i - 1 >= 0 and j-1 >= 0 and board[i-1][j-1] == 1:
                    neighbors += 1
                if i - 1 >= 0 and board[i-1][j] == 1:
                    neighbors += 1
                if i - 1 >= 0 and j + 1 < len_row and board[i-1][j+1] == 1:
                    neighbors += 1
                if j -1 >= 0 and board[i][j-1] == 1:
                    neighbors += 1
                if j+1 < len_row and board[i][j+1] == 1:
                    neighbors += 1
                if i +1 < len_board and j - 1 >= 0 and board[i+1][j-1] == 1:
                    neighbors += 1
                if i + 1 < len_board and board[i+1][j] == 1:
                    neighbors += 1
                if i + 1 < len_board and j + 1 < len_row and  board[i+1][j+1] == 1:
                    neighbors += 1

                if board[i][j] == 1 and neighbors < 2:
                    ans[i][j] = 0
                elif board[i][j] == 1 and neighbors in (2,3):
                    ans[i][j] = 1
                elif board[i][j] == 1 and neighbors > 3:
                    ans[i][j] = 0
                elif board[i][j] == 0 and neighbors == 3:
                    ans[i][j] = 1

        for i in range(len_board):
            for j in range(len_row):
                board[i][j] = ans[i][j]

s = Solution()

matrix=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(matrix)
print(matrix, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
matrix=[[1,1],[1,0]]
s.gameOfLife(matrix)
print(matrix, [[1,1],[1,1]])
