#https://leetcode.com/problems/validate-binary-search-tree


from typing import Optional, List

def insert_level_order(arr, root, i, n):
    if i < n:
        if arr[i] is None:
            return None
        temp = TreeNode(arr[i])
        root = temp

        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def create_bst_from_list(arr):
    if not arr:
        return None
    return insert_level_order(arr, None, 0, len(arr))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def _inorder(node: Optional[TreeNode]):
            res = []
            if node:
                res = _inorder(node.left)
                res.append(node.val)
                res = res + _inorder(node.right)
            return res

        res = _inorder(root)

        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False

        return True
    
s = Solution()

print(s.isValidBST(create_bst_from_list([2,1,3])), True)
print(s.isValidBST(create_bst_from_list([5,1,4,None,None,3,6])), False)