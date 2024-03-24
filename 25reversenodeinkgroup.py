from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = tmpNode = ListNode(0)

        nodearray = []
        while head:
            nodearray.append(head.val)
            head = head.next

        while len(nodearray) > 0:

            if len(nodearray) >= k:
                for i in range(0, k):
                    tmpNode.next = ListNode(nodearray.pop((k - 1) - i))
                    tmpNode = tmpNode.next
            else:
                for na in nodearray:
                    tmpNode.next = ListNode(nodearray.pop(0))
                    tmpNode = tmpNode.next

        return result.next

s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(s.reverseKGroup(n1, 3))
print(s.reverseKGroup(n1, 2))