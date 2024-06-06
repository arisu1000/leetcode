#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree


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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    lca = None

    def findNode(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if root is None:
            return 0

        ans = 0
        if root == p or root == q:
            ans = 1

        if root.left:
            ans += self.findNode(root.left, p, q)
        if root.right:
            ans += self.findNode(root.right, p, q)

        if ans == 2 and self.lca is None:
            self.lca = root

        return ans
        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.findNode(root, p, q)

        return self.lca



    

s = Solution()
root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
s.lowestCommonAncestor(root, root.left, root.right)
s.lowestCommonAncestor(root, root.left, root.left.right.right)

root = build_tree([1,2])
s.lowestCommonAncestor(root, root, root.left)
