from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(nums):
    if not nums:
        return None
    nodes = [ListNode(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]
 

def listNode(node):
    list = []

    if node == None:
        return list

    while node.next is not None:
        list.append(node.val)
        node = node.next

    list.append(node.val)

    return list

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k == 0:
            return head
        
        tempHead = head
        length = 0
        while tempHead is not None:
            length += 1
            tempHead = tempHead.next

        k = k%length
        
        if k == 0:
            return head


        tempHead = head
        for i in range(k):
            current = ListNode(-101)
            ans = current
            while tempHead is not None:
                if tempHead.next is not None:
                    current.next = tempHead
                    current = current.next
                else:
                    current.next = None
                    current = ListNode(tempHead.val, ans.next)
                    ans = current

                tempHead = tempHead.next
            
            tempHead = ans

        return ans


s = Solution()
print(listNode(s.rotateRight(create_linked_list([1]), 1)), [1])
print(listNode(s.rotateRight(create_linked_list([1,2,3]), 2000000000)), [2,3,1])
print(listNode(s.rotateRight(create_linked_list([]), 0)), [])
print(listNode(s.rotateRight(create_linked_list([1,2,3,4,5]), 2)), [4,5,1,2,3])
print(listNode(s.rotateRight(create_linked_list([0,1,2]), 4)), [2,0,1])