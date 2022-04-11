
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        if head.next != None:
            count = 1

        node = head
        nodes = []
        nodes.append(node)
        while node.next != None:
            count += 1
            node = node.next
            nodes.append(node)

        result = None
        
        for i in range(count, 0, -1):
            member = nodes.pop()
            if count - i+1 != n:
                ln = ListNode(member.val, result)
                result = ln
        
        return result

s = Solution()

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1, None)
l3 = ListNode(1, ListNode(2, None))


print(s.removeNthFromEnd(l1, 2))
# print(s.removeNthFromEnd([1], 1))
# print(s.removeNthFromEnd([1,2], 1))