#https://leetcode.com/problems/word-search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, index):
            nonlocal result 

            if len(word) > 0 and index == len(word) - 1:
                if board[row][col] == word[index]:
                    result = True
                return
            
            if board[row][col] == word[index]:
                temp = board[row][col]
                board[row][col] = '#'
                if row - 1 > -1:
                    backtrack(row - 1, col, index+1)
                
                if row + 1 < row_len:
                    backtrack(row + 1, col, index+1)
                
                if col - 1 > -1:
                    backtrack(row, col - 1, index+1)

                if col + 1 < col_len:
                    backtrack(row, col + 1, index+1)

                board[row][col] = temp
            else:
                return

        result = False
        row_len = len(board)
        col_len = len(board[0])
        for row in range(row_len):
            for col in range(col_len):
                backtrack(row, col, 0)
                if result:
                    return result

        return False
    
s = Solution()


board = [["a","b"]]
word = "ba"
print(s.exist(board, word), True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board, word), False)


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(s.exist(board, word), True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board, word), True)
