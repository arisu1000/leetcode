#https://leetcode.com/problems/reverse-linked-list-ii

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        newHead = ListNode(-600)
        ans = newHead
        
        count = 1
        while head is not None:
            
            if count < left:
                ans.next = ListNode(head.val)
                ans = ans.next
            elif count > right:
                if count - right == 1:
                    tempHead = newHead 
                    while tempHead.next is not None:
                        tempHead = tempHead.next
                    tempHead.next = ans
                
                while ans.next is not None:
                    ans = ans.next

                ans.next = ListNode(head.val)
                ans = ans.next
            elif left <= count <= right:
                #뒤집는 로직이 들어가야 한다.
                #val과 next 사이에 새로운걸 끼워 넣어야 한다.
                #새로운걸 만들고 새로운 것의 next에 원래 있던 next를 할당한다.
                #그리고 기존 val의 next에 새로운 노드를 넣는다.
                if left - count == 0:
                    ans = ListNode(head.val, None)
                else:
                    ans = ListNode(head.val, ans)
            
            count += 1
            head = head.next

        if left == 1 and count - 1 == right:
            return ans
        
        if count - right == 1:
            tempHead = newHead 
            while tempHead.next is not None:
                tempHead = tempHead.next
            tempHead.next = ans

        return newHead.next
        

s = Solution()


print(listNode(s.reverseBetween(create_linked_list([1,2,3]), 2, 3)), [1,3,2])
print(listNode(s.reverseBetween(create_linked_list([1,2,3]), 1, 2)), [2,1,3])
print(listNode(s.reverseBetween(create_linked_list([3,5]), 1, 2)),[5,3])
print(listNode(s.reverseBetween(create_linked_list([5]), 1, 1)),[5])
print(listNode(s.reverseBetween(create_linked_list([1,2,3,4,5]), 2, 4)),[1,4,3,2,5])