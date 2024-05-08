#https://leetcode.com/problems/copy-list-with-random-pointer


# Definition for a Node.
# 못풀어서 답보고 했음.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        oldHead = head
        
        ans = {}

        while oldHead != None:
            ans[oldHead] = Node(oldHead.val)
            oldHead = oldHead.next

        oldHead = head
        while oldHead != None:
            if oldHead.next:
                ans[oldHead].next = ans[oldHead.next]
            if oldHead.random:
                ans[oldHead].random = ans[oldHead.random]

            oldHead = oldHead.next

        return ans[head]

s = Solution()


def create_linked_list(nums):
    if not nums:
        return None
    
    nodes = [Node(num[0]) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        if nums[i][1] != None:
            nodes[i].random = nodes[nums[i][1]]
    return nodes[0]
 

s.copyRandomList(create_linked_list([[7,None],[13,0],[11,4],[10,2],[1,0]]))