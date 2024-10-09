# https://leetcode.com/problems/merge-k-sorted-lists

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(lst):
    if not lst:  # 빈 리스트인 경우 처리
        return None

    # 첫 번째 값으로 head 노드 생성
    head = ListNode(lst[0])
    current = head

    # 두 번째 값부터 차례대로 노드 생성 및 연결
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def print_linkedlist(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print('')

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = ListNode()
        head = current

        len_lists = len(lists)
        while lists:
            max_val = 100000
            index = -1
            for i in range(len_lists):
                if lists[i] and lists[i].val <= max_val:
                    max_val = lists[i].val
                    index = i
            
            if index == -1:
                break

            current.next = lists[index]
            lists[index] = lists[index].next
            current = current.next

        return head.next

s = Solution()
mergeList = s.mergeKLists([list_to_linkedlist([1,4,5]),
                           list_to_linkedlist([1,3,4]),
                            list_to_linkedlist([2,6])])

print_linkedlist(mergeList)

mergeList = s.mergeKLists([])

print_linkedlist(mergeList)

mergeList = s.mergeKLists([[]])

print_linkedlist(mergeList)


