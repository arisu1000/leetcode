#https://leetcode.com/problems/spiral-matrix


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        if len(matrix) == 0:
            return ans
        
        RightLimit = len(matrix[0]) - 1
        LeftLimit = 0
        DownLimit = len(matrix) - 1
        UpLimit = 0

        r=0
        c=0
        toRight = True
        toLeft = False
        toDown = False
        toUp = False

        while LeftLimit <= RightLimit and UpLimit <= DownLimit:
                ans.append(matrix[r][c])
                if toRight == True:
                    if RightLimit > c:
                        c += 1
                    else:
                        toRight = False
                        toDown = True
                        UpLimit += 1
                        r += 1
                elif toLeft == True:
                    if LeftLimit < c:
                        c -= 1
                    else:
                        toLeft = False
                        toUp = True
                        DownLimit -= 1
                        r -= 1
                elif toDown == True:
                    if DownLimit > r :
                        r += 1
                    else:
                        toDown = False
                        toLeft = True
                        RightLimit -= 1
                        c -= 1
                elif toUp == True:
                    if UpLimit < r:
                        r -= 1
                    else:
                        toUp = False
                        toRight = True
                        LeftLimit += 1
                        c += 1

        return ans
    
s = Solution()

print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
