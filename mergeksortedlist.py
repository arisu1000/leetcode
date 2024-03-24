from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next\

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        totallists = []
        for l in lists:
            while l:
                totallists.append(l.val)
                l = l.next
        
        totallists.sort()

        tmpnode = ListNode(0)
        result = tmpnode
        for i in totallists:
            tmpnode.next = ListNode(i)
            tmpnode = tmpnode.next

        return result.next

n1 = ListNode(1, ListNode(4, ListNode(5)))
n2 = ListNode(1, ListNode(3, ListNode(4)))
n3 = ListNode(2, ListNode(6))


s = Solution()

# print(s.mergeKLists([]))
# print(s.mergeKLists([ListNode()]))
# print(s.mergeKLists([ListNode(), ListNode()]))
print(s.mergeKLists([n1, n2, n3]))

