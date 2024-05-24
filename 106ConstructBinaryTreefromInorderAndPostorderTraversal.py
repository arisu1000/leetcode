#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

from typing import Optional, List
from collections import deque

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

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(postorder) == 0:
            return None
        
        rootNode = TreeNode(postorder[-1])

        index = inorder.index(postorder[-1])

        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]

        len_left_inorder = len(left_inorder)
        left_postorder = postorder[:len_left_inorder]
        right_postorder = postorder[len_left_inorder:-1]

        leftTree = self.buildTree(left_inorder, left_postorder)
        rightTree = self.buildTree(right_inorder, right_postorder)

        rootNode.left = leftTree
        rootNode.right = rightTree

        return rootNode

s = Solution()

print(tree_to_list(s.buildTree([9,3,15,20,7], [9,15,7,20,3])), [3,9,20,None,None,15,7])
print(tree_to_list(s.buildTree([-1], [-1])), [-1])