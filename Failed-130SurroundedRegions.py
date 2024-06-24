#https://leetcode.com/problems/surrounded-regions

from typing import List

class Solution:

    def isSurround(self, r, c) -> bool:

        if (r < 0 or r >= len(self.board)) or (c < 0 or c >= len(self.board[0])):
            return False

        if self.board[r][c] == 'X':
            return True

        if (r,c) in self.ans:
            return True
        
        if (r,c) in self.visted:
            return False

        self.visted.add((r,c))

        isR1 = self.isSurround(r-1,c)
        isR2 = self.isSurround(r+1,c)
        isR3 = self.isSurround(r,c-1)
        isR4 = self.isSurround(r,c+1)

        if (isR1 and r > 0) and (isR2 and r <= len(self.board)) and (isR3 and c > 0) and (isR4 and c <= len(board[0])):
            self.ans.add((r,c))
            return True

    visted = set()
    ans = set()
    board = []

    def solve(self, board: List[List[str]]) -> None:
        self.visted = set()
        self.board = board
        self.ans = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and not (r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0])-1):
                    
                    self.isSurround(r,c)
                    self.visted.add((r,c))

        for a in self.ans:
            board[a[0]][a[1]] = 'X'




s = Solution()




board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
for b in board:
    print(b)
print([["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

board = [["X","O","X"],
         ["X","O","X"],
         ["X","O","X"]]
s.solve(board)
for b in board:
    print(b)

print([["X","O","X"],["X","O","X"],["X","O","X"]])


board = [["O","O","O"],["O","O","O"],["O","O","O"]]
s.solve(board)
for b in board:
    print(b)

print([["O","O","O"],["O","O","O"],["O","O","O"]])

