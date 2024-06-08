#https://leetcode.com/problems/average-of-levels-in-binary-tree

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

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.ans = []
        self.calculateAvg(root, 0)

        return [val['val']/val['count'] for val in self.ans]

    def calculateAvg(self, node: Optional[TreeNode], depth: int):
        if node is None:
            return 
        
        try:
            self.ans[depth]['val'] += node.val
            self.ans[depth]['count'] += 1
        except IndexError:
            self.ans.append({'val': node.val, 'count': 1})

        if node.left:
            self.calculateAvg(node.left, depth+1)
        if node.right:
            self.calculateAvg(node.right, depth+1)

s = Solution()

print(s.averageOfLevels(build_tree([3,9,20,None,None,15,7])), [3.00000,14.50000,11.00000])
print(s.averageOfLevels(build_tree([3,9,20,15,7])), [3.00000,14.50000,11.00000])
