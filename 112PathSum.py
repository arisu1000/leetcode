#https://leetcode.com/problems/path-sum


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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
        
        return self.calculateSum(root, root.val, targetSum)
    
    def calculateSum(self, current: Optional[TreeNode], partialSum: int, targetSum: int) -> bool:

        leftBoolean = False
        rightBoolean = False

        if current is None:
            return partialSum
        
        if current.left is None and current.right is None:
            return partialSum == targetSum
        
        if current.left is not None:
            leftBoolean = self.calculateSum(current.left, partialSum + current.left.val, targetSum)
        
        if current.right is not None:
            rightBoolean = self.calculateSum(current.right, partialSum + current.right.val, targetSum)

        if leftBoolean or rightBoolean:
            return True
        else:
            return False



s = Solution()        

print(s.hasPathSum(build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22), True)
print(s.hasPathSum(build_tree([1,2,3]), 5), False)
print(s.hasPathSum(build_tree([1]), 1), True)
print(s.hasPathSum(build_tree([]), 0), False)
