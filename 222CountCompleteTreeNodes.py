#https://leetcode.com/problems/count-complete-tree-nodes

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
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        ans = 1
        if root.left:
            ans += self.countNodes(root.left)

        if root.right:
            ans += self.countNodes(root.right)
    
        return ans
    
s = Solution()
print(s.countNodes(build_tree([1,2,3,4,5,6])), 6)
print(s.countNodes(build_tree([])), 0)
print(s.countNodes(build_tree([1])), 1)