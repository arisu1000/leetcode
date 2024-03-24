from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        count = 1
        startRow = 0
        endRow = n - 1
        startCol = 0
        endCol = n - 1

        while count <= n*n:
            #오른쪽
            for i in range(startCol, endCol + 1):
                if result[startRow][i] == 0:
                    result[startRow][i] = count
                    count += 1
                else:
                    break
                
            #아래로
            for i in range(startRow+1, endRow + 1):
                if result[i][endCol] == 0:
                    result[i][endCol] = count
                    count += 1
                else:
                    break

            #왼쪽으로
            for i in range(endCol - 1, startCol - 1, -1):
                if result[endRow][i] == 0:
                    result[endRow][i] = count
                    count += 1
                else:
                    break
            #위로
            for i in range(endRow - 1, startRow, -1):
                if result[i][startCol] == 0:
                    result[i][startCol] = count
                    count += 1
                else:
                    break

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1

        return result
    

s = Solution()
print(s.generateMatrix(4))

