#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = ListNode(-101)
        ans = current

        isDuplicated = False
        while head is not None:
            if head.next is not None:
                if head.val == head.next.val:
                    head = head.next
                    isDuplicated = True
                    continue
            
            if isDuplicated == True:
                head = head.next
                isDuplicated = False
                
            else:
                current.next = head
                current = current.next
                head = head.next
        
        current.next = head

        return ans.next
    
s = Solution()

print(listNode(s.deleteDuplicates(create_linked_list([1,2,2]))), [1])
print(listNode(s.deleteDuplicates(create_linked_list([1,2,3,3,4,4,5]))), [1,2,5])
print(listNode(s.deleteDuplicates(create_linked_list([1,1,1,2,3]))),[2,3])