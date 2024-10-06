# https://leetcode.com/problems/sort-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(lst):
    if not lst:  # 빈 리스트 처리
        return None

    # 첫 번째 값을 이용해 첫 번째 노드(head) 생성
    head = ListNode(lst[0])
    current = head

    # 두 번째 값부터 노드를 생성해 연결
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next  # 다음 노드로 이동

    return head

# 링크드 리스트를 출력하는 함수
def print_linkedlist(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def list_to_linkedlist(lst):
            if not lst:  # 빈 리스트 처리
                return None

            # 첫 번째 값을 이용해 첫 번째 노드(head) 생성
            head = ListNode(lst[0])
            current = head

            # 두 번째 값부터 노드를 생성해 연결
            for value in lst[1:]:
                current.next = ListNode(value)
                current = current.next  # 다음 노드로 이동

            return head


        tmp_list = []
        node = head
        while node:
            tmp_list.append(node.val)
            node = node.next
        
        tmp_list.sort()

        new_node = list_to_linkedlist(tmp_list)

        return new_node
    

s = Solution()
input = list_to_linkedlist([4,2,1,3])
print_linkedlist(s.sortList(input))

input = list_to_linkedlist([-1,5,3,4,0])
print_linkedlist(s.sortList(input))

