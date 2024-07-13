#https://leetcode.com/problems/course-schedule-ii

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 그래프와 진입 차수를 최고하합니다.
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        #그래프와 진입 차수를 구축합니다.
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        #진입 차수가 0인 노드를 큐에 추가합니다.
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        #BFS를 통해 그래프를 탐색하며 위상 정렬을 수행합니다.
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 모든 노드를 방문할 수 있으면 순환이 없는 것입니다.
        if len(order) == numCourses:
            return order
        else:
            return []
    

s = Solution()

print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])
print(s.findOrder(2, [[1,0]]), [0,1])
print(s.findOrder(1, []), [0])
