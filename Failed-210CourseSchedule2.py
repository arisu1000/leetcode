#https://leetcode.com/problems/course-schedule-ii

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if len(prerequisites) == 0:
            return [0]

        orderList = []

        for p in prerequisites:
            
            if len(orderList) == 0:
                orderList.append(p[1])
                orderList.append(p[0])

            for idx, value in enumerate(orderList):

        return orderList
    
    

s = Solution()

print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])
print(s.findOrder(2, [[1,0]]), [0,1])
print(s.findOrder(1, []), [0])
