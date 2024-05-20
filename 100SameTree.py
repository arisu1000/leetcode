#https://leetcode.com/problems/same-tree

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
    
        isLeftSame = False
        isRightSame = False
        if p is not None:
            if q is None:
                return False
            elif q is not None:
                if p.val == q.val:
                    if p.left is not None and q.left is not None:
                        isLeftSame = self.isSameTree(p.left, q.left)
                    elif p.left is None and q.left is None:
                        isLeftSame = True
                    if p.right is not None and q.right is not None:
                        isRightSame = self.isSameTree(p.right, q.right)
                    elif p.right is None and q.right is None:
                        isRightSame = True
                else:
                    return False        
                
        elif q is not None:
                return False

        return isLeftSame == True and isRightSame == True
    
s = Solution()
print(s.isSameTree(build_tree([1,2,3]), build_tree([1,2,3])), True)
print(s.isSameTree(build_tree([1,2]), build_tree([1,None,2])), False)
print(s.isSameTree(build_tree([1,2,1]), build_tree([1,1,2])), False)