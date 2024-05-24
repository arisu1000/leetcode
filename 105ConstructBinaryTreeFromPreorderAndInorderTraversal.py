#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

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

#preorder의 첫번째를 inorder에서 찾으면 항상 절반으로 나눌 수 있으니까 거기서 부터 재귀로 돈다.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0:
            return None

        rootNode = TreeNode(preorder[0])

        index = inorder.index(preorder[0])
        left = inorder[:index]
        right = inorder[index+1:]
        
        len_left = len(left)

        left_preorder = preorder[1:len_left+1]
        right_preorder = preorder[len_left+1:]

        leftTree = self.buildTree(left_preorder, left)
        rightTree = self.buildTree(right_preorder, right)

        rootNode.left = leftTree
        rootNode.right = rightTree

        return rootNode
        



s = Solution()
print(tree_to_list(s.buildTree([1,2], [1,2])), [1,None,2])
print(tree_to_list(s.buildTree([3,9,20,15,7], [9,3,15,20,7])), [3,9,20,None,None,15,7])