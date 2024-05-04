#https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from  typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        
        exist = set()
        while head.next != None:
            if head in exist:
                return True
            
            exist.add(head)
            head = head.next

        return False


s = Solution()


def create_linked_list(nums, pos):
    if not nums:
        return None
    nodes = [ListNode(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

print(s.hasCycle(create_linked_list([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5], -1)), False)
print(s.hasCycle(create_linked_list([], -1)), False)
print(s.hasCycle(create_linked_list([3, 2, 0, -4], 1)), True)
print(s.hasCycle(create_linked_list([1,2],0)), True)
print(s.hasCycle(create_linked_list([1], -1)), False)
