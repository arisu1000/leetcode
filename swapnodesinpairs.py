from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmpNode = ListNode(0)
        resultNode = tmpNode 

        listarray = []
        while head:
            listarray.append(head.val)
            head = head.next
        
        while len(listarray) > 0:
            first = listarray.pop(0)
            if len(listarray) > 0:
                second = listarray.pop(0)

                tmpNode.next = ListNode(second, next=ListNode(first))
                tmpNode = tmpNode.next
                tmpNode = tmpNode.next
            else:
                tmpNode.next = ListNode(first)
                tmpNode = tmpNode.next

        return resultNode.next

s = Solution()

l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
l0 = ListNode()


# print(s.swapPairs(l0))
print(s.swapPairs(ListNode(1)))
print(s.swapPairs(l1))
