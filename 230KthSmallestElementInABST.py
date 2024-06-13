#https://leetcode.com/problems/kth-smallest-element-in-a-bst

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

    def inorderTree(self, root: Optional[TreeNode], k: int) -> List:
        res = []

        if root:
            res = self.inorderTree(root.left, k)
            if len(res) >= k:
                return res
            res.append(root.val)
            res = res + self.inorderTree(root.right, k)

        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = self.inorderTree(root, k)
        return ans[k-1]
    
s = Solution()
print(s.kthSmallest(create_bst_from_list([3,1,4,None,2]), 1), 1)
print(s.kthSmallest(create_bst_from_list([5,3,6,2,4,None,None,1]), 3), 3)