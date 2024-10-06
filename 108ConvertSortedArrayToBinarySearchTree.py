#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.

from typing import List, Optional
from collections import deque


def level_order_traversal(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val)  # 현재 노드 값 출력
        
        if node.left:
            queue.append(node.left)  # 왼쪽 자식 노드를 큐에 추가
        if node.right:
            queue.append(node.right)  # 오른쪽 자식 노드를 큐에 추가


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums) == 0:
            return

        mid_index =  len(nums) // 2
        
        node = TreeNode(nums[mid_index])
        node.left = self.sortedArrayToBST(nums[:mid_index])
        node.right = self.sortedArrayToBST(nums[mid_index+1:])

        return node
    

s = Solution()
level_order_traversal(s.sortedArrayToBST([1,3]))
level_order_traversal(s.sortedArrayToBST([-10,-3,0,5,9]))


