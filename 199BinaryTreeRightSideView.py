#https://leetcode.com/problems/binary-tree-right-side-view


from typing import Optional, List
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

    ans = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        self.ans=[]
        self.findNode(root, 0, 0)
        self.findNode(root, 0, 0)
        return [val['val'] for val in self.ans]

    def findNode(self, node: Optional[TreeNode], depth, x):
        if node is None:
            return

        try:
            self.ans[depth]['x'] = x
            self.ans[depth]['val'] = node.val
        except IndexError:
            self.ans.append({'x': x, 'val': node.val})

        if node.left:
            self.findNode(node.left, depth + 1, x - (100 + depth))
        if node.right:
            self.findNode(node.right, depth + 1, x + (100 + depth))

s = Solution()

print(s.rightSideView(build_tree([0,1,2,None,3,4,None,  None, None,None,5,9,None,None,None, None,None,None,None,None,None,None,6,10,None])), [0,2,4,9,10])
print(s.rightSideView(build_tree([1,2,3,None,5,None,4])), [1,3,4])
print(s.rightSideView(build_tree([1,None,3])), [1,3])
print(s.rightSideView(build_tree([])),[])