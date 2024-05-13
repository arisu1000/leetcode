#https://leetcode.com/problems/reverse-nodes-in-k-group/

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ans = ListNode(-1)

        count = 0
        current = ListNode(-1)
        while head is not None:
            if count < k:
                if current.val == -1:
                    current = ListNode(head.val)
                else:
                    current = ListNode(head.val, current)
                count += 1

                head = head.next
            else:
                tempAns = ans
                while tempAns.next is not None:
                    tempAns = tempAns.next

                tempAns.next = current
                current = ListNode(-1)
                count = 0

        if current is not None:
            if count < k:
                reverseCurrent = ListNode(-1)
                while current is not None:
                    if reverseCurrent.val == -1:
                        reverseCurrent = ListNode(current.val)
                    else:
                        reverseCurrent = ListNode(current.val, reverseCurrent)

                    current = current.next
            else:
                reverseCurrent = current

        tempAns = ans
        while tempAns.next is not None:
            tempAns = tempAns.next
        
        tempAns.next = reverseCurrent

        return ans.next
        

s = Solution()



print(listNode(s.reverseKGroup(create_linked_list([1,2]), 2)))
print(listNode(s.reverseKGroup(create_linked_list([1,2,3,4,5]), 1)))
print(listNode(s.reverseKGroup(create_linked_list([1,2,3,4,5]), 3)))
print(listNode(s.reverseKGroup(create_linked_list([1,2,3,4,5]), 2)))