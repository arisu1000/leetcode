from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # #경우의 수를 찾아야 하는 문제
        # #직선과 대각선을 확인하면서 찾아야 함.
        # #한군데 놓고, 그 다음행에서 찾으면 됨.

        # result = []


        # row_list = [["." for k in range(n)] for i in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         #첫번째 행에 값 집어 넣기
        #         row_list[i][j] = "Q"
        #         # print(row_list)
        #         #행렬 전체에서 안되는 것들 마킹하기
        #         for i2 in range(n):
        #             for j2 in range(n):
        #                 if (i == i2 and j!= j2) or (i != i2 and j==j2):
        #                     row_list[i2][j2] = "x"
                
        #         # 그 다음행에서 x가 아닌 것들 중에서 Q마킹하기
        #         for j3 in range(n):
        #             if j != j3 and row_list[i+1][j3] == ".":
        #                 row_list[i+1][j3] = "Q"
                
        #         print(row_list)
        # return []

        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        queens = []

        def isSafe(queens, row, col):
            for r, c in queens:
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True
        
        def solveNQueensHelper(row):
            nonlocal result
            if row == n:
                result.append([''.join(row) for row in board])
            
                return
            
            for col in range(n):
                if isSafe(queens, row, col):
                    board[row][col] = 'Q'
                    queens.append((row, col))
                    # print(board, queens)
                    solveNQueensHelper(row + 1)
                    board[row][col] = '.'
                    queens.pop()
        
        solveNQueensHelper(0)
        return len(result)

s = Solution()
print(s.solveNQueens(4))