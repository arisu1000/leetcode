#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal


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

    def makeList(self, node: Optional[TreeNode], depth):

        if node is None:
            return
        
        try:
            if depth % 2 == 0:
                self.ans[depth].append(node.val)
            else:
                self.ans[depth].insert(0, node.val)
        except IndexError:
            self.ans.append([node.val])

        if node.left:
            self.makeList(node.left, depth + 1)
        if node.right:
            self.makeList(node.right, depth + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.makeList(root, 0)
        return self.ans
    
s = Solution()
print(s.zigzagLevelOrder(build_tree([1,2,3,4,None,None,5])), [[1],[3,2],[4,5]])
print(s.zigzagLevelOrder(build_tree([3,9,20,None,None,15,7])), [[3],[20,9],[15,7]])
print(s.zigzagLevelOrder(build_tree([1])), [[1]])
print(s.zigzagLevelOrder(build_tree([])), [])