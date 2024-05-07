#https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        ans = head
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                while ans.next is not None:
                    ans = ans.next
                ans.next = ListNode(list1.val)
                list1 = list1.next
            else:
                while ans.next is not None:
                    ans = ans.next
                ans.next = ListNode(list2.val)
                list2 = list2.next

        while list1 != None:
            while ans.next is not None:
                ans = ans.next
            ans.next = ListNode(list1.val)
            list1 = list1.next

        while list2 != None:
            while ans.next is not None:
                ans = ans.next
            ans.next = ListNode(list2.val)
            list2 = list2.next

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

    if node == None:
        return list

    while node.next is not None:
        list.append(node.val)
        node = node.next

    list.append(node.val)

    return list



print(listNode(s.mergeTwoLists(create_linked_list([1]),create_linked_list([]))))
print(listNode(s.mergeTwoLists(create_linked_list([1,2,4]),create_linked_list([1,3,4]))))
print(listNode(s.mergeTwoLists(create_linked_list([]),create_linked_list([]))))
print(listNode(s.mergeTwoLists(create_linked_list([]),create_linked_list([0]))))
