from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or head == None or head.next == None:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        k %= length
        if k==0:
            return head

        firstNode = head
        for _ in range(length - k - 1):
            firstNode = firstNode.next
        
        new_head = firstNode.next
        firstNode.next = None
        tail.next = head

        return new_head    
        
        

n1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
print(s.rotateRight(n1, 2))