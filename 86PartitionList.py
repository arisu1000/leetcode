#https://leetcode.com/problems/partition-list

from typing import Optional

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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lower_current = ListNode(-101)
        lower = lower_current
        higher_current = ListNode(-101)
        higher = higher_current

        while head is not None:
            if head.val < x:
                lower_current.next = head
                lower_current = lower_current.next
            else:
                higher_current.next = head
                higher_current = higher_current.next
            
            head = head.next

        lower_current.next = higher.next
        higher_current.next = None

        return lower.next

s = Solution()

print(listNode(s.partition(create_linked_list([1,4,3,2,5,2]), 3)), [1,2,2,4,3,5])
print(listNode(s.partition(create_linked_list([2,1]), 2)), [1,2])