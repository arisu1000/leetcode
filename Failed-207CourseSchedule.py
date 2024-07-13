#https://leetcode.com/problems/course-schedule

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프를 초기화합니다.
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # 그래프를 구축하고 진입 차수를 계산합니다.
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # 진입 차수가 0인 노드를 큐에 추가합니다.
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        # BFS를 통해 그래프를 탐색합니다.
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 모든 노드를 방문할 수 있으면 순환이 없는 것입니다.
        return visited == numCourses


s = Solution()
print(s.canFinish(3, [[1,0],[0,2],[2,1]]), False)
print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]), False)
print(s.canFinish(2, [[1,0]]), True)
print(s.canFinish(2, [[1,0],[0,1]]), False)
print(s.canFinish(3, [[1,0]]), True)
print(s.canFinish(3, [[0,1],[0,2],[1,2]]), True)

