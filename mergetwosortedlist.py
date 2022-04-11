from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         result = ListNode()
#         nodelist = []

#         if list1 == None:
#             return list2
#         elif list2 == None:
#             return list1

#         while list1 != None:
#             while list2 != None:

#                 if list1 == None:
#                     nodelist.append(list2)
#                     list2 = list2.next
#                 elif list1.val <= list2.val:
#                     nodelist.append(list1)
#                     list1 = list1.next
#                 else:
#                     nodelist.append(list2)
#                     list2 = list2.next
            
#             if list1 != None:
#                 nodelist.append(list1)
#                 list1 = list1.next

#         result = None
#         for i in range(len(nodelist), 0, -1):
#             node = nodelist.pop()
#             ln = ListNode(node.val, result)
#             result = ln

#         return result


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # dummy = ListNode(0)  
        # cur = dummy  
        cur = ListNode(0)
        while l1 and l2:  
            if l1.val <= l2.val:  
                cur.next = l1  
                l1 = l1.next  
            else:  
                cur.next = l2  
                l2 = l2.next  
            cur = cur.next  
        cur.next = l1 or l2  
  
        return cur.next  

s = Solution()

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

l3 = ListNode(5)
l4 = ListNode(1, ListNode(2, ListNode(4)))

print(s.mergeTwoLists(l1, l2))
print(s.mergeTwoLists(l3, l4))
# print(s.mergeTwoLists(None, None))
# print(s.mergeTwoLists(ListNode(), ListNode(0)))
