#https://leetcode.com/problems/symmetric-tree

from typing import Optional

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


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        #left, right를 내려가면서 바꿔서 계속 비교
        return self.check(root.left, root.right)
    

    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False
        
        outside = self.check(left.left, right.right)
        inside = self.check(left.right, right.left)

        if outside == True and inside == True:
            return True
        else:
            return False


s = Solution()
print(s.isSymmetric(build_tree([1,2,2,3,4,4,3])), True)
print(s.isSymmetric(build_tree([1,2,2,None,3,None,3])), False)