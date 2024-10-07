# https://leetcode.com/problems/construct-quad-tree

from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        # Helper function to check if the grid is uniform
        def isUniform(grid, r1, c1, r2, c2):
            first_val = grid[r1][c1]
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] != first_val:
                        return False
            
            return True
        
        # Recursive function to construct the quad tree
        def buildQuadTree(r1, c1, r2, c2):
            if isUniform(grid, r1, c1, r2, c2):
                return Node(grid[r1][c1] == 1, True, None, None, None, None)

            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2

            return Node(True, False,
                buildQuadTree(r1, c1, mid_r, mid_c),
                buildQuadTree(r1, mid_c, mid_r, c2),
                buildQuadTree(mid_r, c1, r2, mid_c),
                buildQuadTree(mid_r, mid_c, r2, c2)
                )

        return buildQuadTree(0, 0, len(grid), len(grid))
    

s = Solution()

grid = [[0,1],[1,0]]
quadNode = s.construct(grid)
print(quadNode,[[0,1],[1,0],[1,1],[1,1],[1,0]])

grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
quadNode = s.construct(grid)
print(quadNode,[[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]])

