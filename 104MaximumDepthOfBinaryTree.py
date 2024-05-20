#https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftDepth, rightDepth = 1, 1
        if root.left is not None:
            leftDepth = 1
            leftSubDepth = self.maxDepth(root.left)
            leftDepth += leftSubDepth
        if root.right is not None:
            rightDepth = 1
            rightSubDepth = self.maxDepth(root.right)
            rightDepth += rightSubDepth

        return max(leftDepth, rightDepth)
    
    


s = Solution()

print(s.maxDepth(build_tree([3,9,20,None,None,15,7])), 3)
print(s.maxDepth(build_tree([1,None,2])), 2)
