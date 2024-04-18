#https://leetcode.com/problems/valid-sudoku

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #모든 열은 1에서 9까지의 값을 중복없이 가져야 한다.
        #모든 행은 1에서 9까지의 값을 중복없이 가져야 한다.
        #3x3 square는 1에서 9까지의 값을 가져야 한다.

        subBox01 = [0,0,0,0,0,0,0,0,0]
        subBox02 = [0,0,0,0,0,0,0,0,0]
        subBox03 = [0,0,0,0,0,0,0,0,0]
        subBox04 = [0,0,0,0,0,0,0,0,0]
        subBox05 = [0,0,0,0,0,0,0,0,0]
        subBox06 = [0,0,0,0,0,0,0,0,0]
        subBox07 = [0,0,0,0,0,0,0,0,0]
        subBox08 = [0,0,0,0,0,0,0,0,0]
        subBox09 = [0,0,0,0,0,0,0,0,0]

        for r in range(9):
            rowCheck = [0,0,0,0,0,0,0,0,0]
            columnCheck = [0,0,0,0,0,0,0,0,0]

            for c in range(9):

                #행 체크
                if board[r][c] != ".":
                    index = int(board[r][c]) - 1
                    rowCheck[index] += 1
                    if rowCheck[index] > 1:
                        return False
                    
                    if r in [0,1,2] and c in [0,1,2]:
                        subBox01[index] += 1
                        if subBox01[index] > 1:
                            return False
                    elif  r in [0,1,2] and c in [3,4,5]:                        
                        subBox02[index] += 1
                        if subBox02[index] > 1:
                            return False
                    elif  r in [0,1,2] and c in [6,7,8]:                        
                        subBox03[index] += 1
                        if subBox03[index] > 1:
                            return False
                    if r in [3,4,5] and c in [0,1,2]:
                        subBox04[index] += 1
                        if subBox04[index] > 1:
                            return False
                    elif  r in [3,4,5] and c in [3,4,5]:                        
                        subBox05[index] += 1
                        if subBox05[index] > 1:
                            return False
                    elif  r in [3,4,5] and c in [6,7,8]:                        
                        subBox06[index] += 1
                        if subBox06[index] > 1:
                            return False
                    if r in [6,7,8] and c in [0,1,2]:
                        subBox07[index] += 1
                        if subBox07[index] > 1:
                            return False
                    elif  r in [6,7,8] and c in [3,4,5]:                        
                        subBox08[index] += 1
                        if subBox08[index] > 1:
                            return False
                    elif  r in [6,7,8] and c in [6,7,8]:                        
                        subBox09[index] += 1
                        if subBox09[index] > 1:
                            return False
                    
                #열 체크
                if board[c][r] != ".":
                    index = int(board[c][r]) - 1
                    columnCheck[index] += 1
                    if columnCheck[index] > 1:
                        return False
       
        return True

s = Solution()

print(s.isValidSudoku([[".",".",".",".","5",".",".","1","."],
                       [".","4",".","3",".",".",".",".","."],
                       [".",".",".",".",".","3",".",".","1"],
                       ["8",".",".",".",".",".",".","2","."],
                       [".",".","2",".","7",".",".",".","."],
                       [".","1","5",".",".",".",".",".","."],
                       [".",".",".",".",".","2",".",".","."],
                       [".","2",".","9",".",".",".",".","."],
                       [".",".","4",".",".",".",".",".","."]]), False)

print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]), True)

print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]), False)

