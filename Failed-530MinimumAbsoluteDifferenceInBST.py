#https://leetcode.com/problems/minimum-absolute-difference-in-bst


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

    def inorderTraversal(self, root) -> List:
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 100000000
        res = self.inorderTraversal(root)

        ans = 100000000
        for i in range(1, len(res)):
            ans = min(ans, abs(res[i] - res[i-1]))

        return ans
    
s = Solution()


print(s.getMinimumDifference(build_tree([543,384,652,None,445,None,699])), 47)
print(s.getMinimumDifference(build_tree([334,277,507,None,285,None,678])), 8)
print(s.getMinimumDifference(build_tree([236,104,701,None,227,None,911])), 9)
print(s.getMinimumDifference(build_tree([4,2,6,1,3])), 1)
print(s.getMinimumDifference(build_tree([1,0,48,None,None,12,49])), 1)