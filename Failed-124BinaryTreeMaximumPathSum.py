#https://leetcode.com/problems/binary-tree-maximum-path-sum
#실패해서 다른 답을 참조했음. 다시 풀어봐야 함.

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
    maxSum = -10000000
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 
        
        self.calculateSum(root)

        return self.maxSum
    
    def calculateSum(self, current: Optional[TreeNode]) -> {}:
        if current is None:
            return 0

        leftSum = max(self.calculateSum(current.left), 0)
        rightSum = max(self.calculateSum(current.right), 0)

        sum = current.val + leftSum + rightSum

        self.maxSum = max(self.maxSum, sum)

        return current.val + max(leftSum, rightSum)



s = Solution()
print(s.maxPathSum(build_tree([5,4,8,11,None,13,4,7,2,None,None,None,None,None,1])), 48)
s = Solution()
print(s.maxPathSum(build_tree([2,-1])), 2)
s = Solution()
print(s.maxPathSum(build_tree([1,2,3])), 6)
s = Solution()
print(s.maxPathSum(build_tree([-10,9,20,None,None,15,7])), 42)