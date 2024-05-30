#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is None:
            return None

        temp = Node(arr[i])
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
            result.append(node.next)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root is None:
            return root
        
        self.makeNext(root)

        return root
    
    def makeNext(self, current):
        if current is None:
            return None
        
        if current.left != None:
            if current.right != None:
                current.left.next = current.right
            else:
                currentNext = current.next
                while currentNext != None:
                    if currentNext.left != None:
                        current.left.next = currentNext.left
                        break
                    elif currentNext.right != None:
                        current.left.next = currentNext.right
                        break
                    else:
                        currentNext = currentNext.next
        
        if current.right != None:
            currentNext = current.next
            while currentNext != None:
                if currentNext.left != None:
                    current.right.next = currentNext.left
                    break
                elif currentNext.right != None:
                    current.right.next = currentNext.right
                    break
                else:
                    currentNext = currentNext.next
                                    
        self.makeNext(current.left)
        self.makeNext(current.right)
        self.makeNext(current.left)
    

    
    

s = Solution()
# print(tree_to_list(s.connect( build_tree([-9,-3,2,None,4,4,0,-6,None,-5]))), [-9,None,-3,2,None,4,4,0,None,-6,-5,None])
print(tree_to_list(s.connect( build_tree([2,1,3,0,7,9,1,2,None,1,0,None,None,8,8,None,None,None,None,7]))), [2,None,1,3,None,0,7,9,1,None,2,1,0,8,8,None,7,None])
# print(tree_to_list(s.connect( build_tree([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5]))), [1,None,2,2,None,3,3,3,3,None,4,4,4,4,4,4,None,5,5,None])
# print(tree_to_list(s.connect( build_tree([0,2,4,1,None,3,-1,5,1,None,6,None,8]))), [0,None,2,4,None,1,3,-1,None,5,1,6,8,None])
# print(tree_to_list(s.connect( build_tree([3,9,20,None,None,15,7]))), [3,None,9,20,None,15,7,None])
print(tree_to_list(s.connect( build_tree([1,2,3,4,None,None,5]))), [1,None,2,3,None,4,5,None])
print(tree_to_list(s.connect( build_tree([1,2,3,4,5,None,7]))), [1,None,2,3,None,4,5,7,None])
print(tree_to_list(s.connect( build_tree([]))), [])