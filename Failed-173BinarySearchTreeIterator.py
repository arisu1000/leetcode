#https://leetcode.com/problems/binary-search-tree-iterator


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

class BSTIterator:

    leftChecked = 'leftChecked'
    node = 'node'

    root = TreeNode()
    parent = {node: None, leftChecked: False}
    current = {node: None, leftChecked: False}

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.parent = {self.node: None, self.leftChecked: False}
        self.current = {self.node: None, self.leftChecked: False}

    def next(self) -> int:

        if self.current[self.node] is None:
            self.current[self.node] = self.root

        if self.current[self.node].left:
            if self.current[self.node].left is not None and self.current[self.leftChecked] == False:
                while  self.current[self.node].left is not None and self.current[self.leftChecked] == False:
                    self.parent[self.node] = self.current[self.node]
                    self.current[self.node] = self.current[self.node].left
                    self.current[self.leftChecked] = True
            elif self.current[self.node].left is not None and self.current[self.leftChecked] == True:
                if self.current[self.node].right:
                    self.parent[self.node] = self.current[self.node]
                    self.current[self.node] = self.current[self.node].right      
                    
                    self.current[self.leftChecked] = False
                    while  self.current[self.node].left is not None and self.current[self.leftChecked] == False:
                        self.parent[self.node] = self.current[self.node]
                        self.current[self.node] = self.current[self.node].left
                        self.current[self.leftChecked] = True

                else:
                    self.current[self.node]  = self.parent[self.node] 

        elif self.current[self.node].right:
            self.parent[self.node] = self.current[self.node]
            self.current[self.node] = self.current[self.node].right
        else:
            if self.parent[self.node] is not None:
                self.current[self.node] = self.parent[self.node] 

        return self.current[self.node].val

    def hasNext(self) -> bool:

        if self.parent[self.node] is None:
            if self.current[self.node] is None and self.current[self.leftChecked] == False:
                return True
            return False

        if self.current[self.node].right or (self.parent[self.node].right and self.parent[self.node].right != self.current[self.node]):
            return True
        else:
            return False


tree = build_tree([1])
s = BSTIterator(tree)
print(s.hasNext(), True)
print(s.next(), 1)
print(s.hasNext(), False)



tree = build_tree([7, 3, 15, None, None, 9, 20])
s = BSTIterator(tree)
print(s.next(), 3)
print(s.next(), 7  )
print(s.hasNext(), True)
print(s.next(), 9)
print(s.hasNext(), True)
print(s.next(), 15)
print(s.hasNext(), True)
print(s.next(), 20)
print(s.hasNext(), False)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()