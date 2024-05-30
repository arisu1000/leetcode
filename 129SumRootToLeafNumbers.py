#https://leetcode.com/problems/sum-root-to-leaf-numbers


from typing import Optional
from collections import deque

def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is None:
            return None

        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
    return root

def build_tree(arr):
    n = len(arr)
    if n == 0:
        return None
    return insert_level_order(arr, None, 0, n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        pathNumberStr = ""
        totalsum = 0

        def makePathNumber(current: Optional[TreeNode], pathNumberStr: str) -> str:
            nonlocal totalsum
            if current.left is None and current.right is None:
                pathNumberStr += str(current.val)
                totalsum += int(pathNumberStr)

            if current.left is not None:
                makePathNumber(current.left, pathNumberStr + str(current.val))
            
            if current.right is not None:
                makePathNumber(current.right, pathNumberStr + str(current.val))

        makePathNumber(root, pathNumberStr)

        return totalsum

s = Solution()
print(s.sumNumbers(build_tree([1,2,3])), 25)        
print(s.sumNumbers(build_tree([4,9,0,5,1])), 1026)        