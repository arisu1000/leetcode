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
        
        ans = self.makeNext(root, None, None)

        return ans
    
    def makeNext(self, left: 'Node', right: 'Node', parent: 'Node') -> 'Node':

        if left is None:
            if right is None:
                return left
            else:
                tmpParent = parent
                while tmpParent.next is not None:
                    if tmpParent.next.left is None and tmpParent.next.right is None:
                        tmpParent = tmpParent.next
                        continue

                    if tmpParent.next.left is not None:
                        right.next = tmpParent.next.left
                    else:
                        right.next = tmpParent.next.right
                    break
                
                return right
        
        if right is None:
            if parent is not None:
                tmpParent = parent
                while tmpParent.next is not None:
                    if tmpParent.next.left is None and tmpParent.next.right is None:
                        tmpParent = tmpParent.next
                        continue

                    if tmpParent.next.left is not None:
                        left.next = tmpParent.next.left
                    else:
                        left.next = tmpParent.next.right
                    break
        else:
            left.next = right

        if right is not None:
            if right.right is None or right.next is None:
                tmpParent = parent
                while tmpParent.next is not None:
                    if tmpParent.next.left is None and tmpParent.next.right is None:
                        tmpParent = tmpParent.next
                        continue

                    if tmpParent.next.left is not None:
                        right.next = tmpParent.next.left
                    else:
                        right.next = tmpParent.next.right
                    break


        if right is not None:
            self.makeNext(right.left, right.right, right)

        self.makeNext(left.left, left.right, left)
        
        
        return left


    

s = Solution()
print(tree_to_list(s.connect( build_tree([-9,-3,2,None,4,4,0,-6,None,-5]))), [-9,None,-3,2,None,4,4,0,None,-6,-5,None])
# print(tree_to_list(s.connect( build_tree([2,1,3,0,7,9,1,2,None,1,0,None,None,8,8,None,None,None,None,7]))), [2,None,1,3,None,0,7,9,1,None,2,1,0,8,8,None,7,None])
# print(tree_to_list(s.connect( build_tree([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5]))), [1,None,2,2,None,3,3,3,3,None,4,4,4,4,4,4,None,5,5,None])
# print(tree_to_list(s.connect( build_tree([0,2,4,1,None,3,-1,5,1,None,6,None,8]))), [0,None,2,4,None,1,3,-1,None,5,1,6,8,None])
# print(tree_to_list(s.connect( build_tree([3,9,20,None,None,15,7]))), [3,None,9,20,None,15,7,None])
# print(tree_to_list(s.connect( build_tree([1,2,3,4,None,None,5]))), [1,None,2,3,None,4,5,None])
# print(tree_to_list(s.connect( build_tree([1,2,3,4,5,None,7]))), [1,None,2,3,None,4,5,7,None])
# print(tree_to_list(s.connect( build_tree([]))), [])