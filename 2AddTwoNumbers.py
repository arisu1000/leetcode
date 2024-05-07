#https://leetcode.com/problems/add-two-numbers

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        addOrder = 0
        head = ListNode(0)
        ans = head
        while l1 != None or l2 != None:
            
            l1Val = 0
            if l1 != None:
                l1Val = l1.val
                l1 = l1.next
            
            l2Val = 0
            if l2 != None:
                l2Val = l2.val
                l2 = l2.next
            
            sum = l1Val + l2Val + addOrder

            if sum >= 10:
                addOrder = 1
                sum = sum % 10
            else:
                addOrder = 0
            
            while ans.next is not None:
                ans = ans.next
            
            ans.next = ListNode(sum)

        if addOrder == 1:
            ans = ans.next
            ans.next = ListNode(addOrder)
            
        return head.next


s = Solution()


def create_linked_list(nums):
    if not nums:
        return None
    nodes = [ListNode(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]
 
def listNode(node):
    list = []
    while node.next is not None:
        list.append(node.val)
        node = node.next

    list.append(node.val)

    return list

print(listNode(s.addTwoNumbers(create_linked_list([2,4,3]), create_linked_list([5,6,4]))), [7,0,8])
print(listNode(s.addTwoNumbers(create_linked_list([0]), create_linked_list([0]))), [0])
print(listNode(s.addTwoNumbers(create_linked_list([9,9,9,9,9,9,9]), create_linked_list([9,9,9,9]))), [8,9,9,9,0,0,0,1])