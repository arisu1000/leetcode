#https://leetcode.com/problems/snakes-and-ladders

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(square):
            row = (square-1) // n
            col = (square-1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col
        
        queue = deque([(1,0)])
        visited = set()

        while queue:
            square, moves = queue.popleft()

            if square == n * n:
                return moves
            
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves +1))

        return -1


s = Solution()

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(s.snakesAndLadders(board))

board = [[-1,-1],[-1,3]]
print(s.snakesAndLadders(board))