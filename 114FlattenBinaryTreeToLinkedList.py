#https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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


def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        
        current = TreeNode(-101)
        self.makeLinkedList(root, current)
        
        root.val = current.right.val
        root.left = None
        root.right = current.right.right

    
    def makeLinkedList(self, node: Optional[TreeNode], current: Optional[TreeNode]) -> None:
        if node is None:
            return

        while current.right is not None:
            current = current.right

        current.right = TreeNode(node.val)
        current.left = None

        self.makeLinkedList(node.left, current.right)
        self.makeLinkedList(node.right, current.right)
        





s = Solution()

print(s.flatten(build_tree([1,2,5,3,4,None,6])), [1,None,2,None,3,None,4,None,5,None,6])
print(s.flatten(build_tree([])), [])
print(s.flatten(build_tree([0])), [0])
