#https://leetcode.com/problems/surrounded-regions

from typing import List

class Solution:

    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'



s = Solution()



board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
for b in board:
    print(b)

print('-------------------------------')
ans = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
for a in ans:
    print(a)
print('-------------------------------')

board = [["X","O","X"],
         ["X","O","X"],
         ["X","O","X"]]
s.solve(board)
for b in board:
    print(b)

print('-------------------------------')
ans = [["X","O","X"],["X","O","X"],["X","O","X"]]
for a in ans:
    print(a)
print('-------------------------------')

board = [["O","O","O"],["O","O","O"],["O","O","O"]]
s.solve(board)
for b in board:
    print(b)

print('-------------------------------')
ans = [["O","O","O"],["O","O","O"],["O","O","O"]]
for a in ans:
    print(a)
print('-------------------------------')
