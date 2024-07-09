#https://leetcode.com/problems/evaluate-division

#chatgpt 솔루션

from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1.0)])
            visited=set()
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product*value))
            
            return -1.0
        
        results=[]
        for a, b in queries:
            results.append(bfs(a,b))

        return results
       

       
    
s = Solution()


print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.0, 0.5, -1.0, 1.0, -1.0 ])

print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), [3.75000,0.40000,5.00000,0.20000])

print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]), [0.50000,2.00000,-1.00000,-1.00000])