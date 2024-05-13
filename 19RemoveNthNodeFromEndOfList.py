#https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = head
        length = 0
        while tempHead is not None:
            length += 1
            tempHead = tempHead.next

        tempHead = head
        current = ListNode(-1)
        ans = current
        while tempHead is not None:
            if length == n:
                current.next = tempHead.next
                current = current.next
                if tempHead.next is None:
                    tempHead = tempHead.next
                else:
                    tempHead = tempHead.next.next
            else:            
                current.next = tempHead
                current = current.next
                tempHead = tempHead.next
            
            length -= 1
            
        return ans.next

s = Solution()

print(listNode(s.removeNthFromEnd(create_linked_list([1,2,3,4,5]), 2)))
print(listNode(s.removeNthFromEnd(create_linked_list([1]), 1)))
print(listNode(s.removeNthFromEnd(create_linked_list([1,2]), 1)))