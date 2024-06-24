#https://leetcode.com/problems/clone-graph


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def create_graph(adj_list):
    if not adj_list:
        return []

    # Step 1: Create all nodes
    nodes = [Node(i + 1) for i in range(len(adj_list))]

    # Step 2: Populate neighbors
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

    return nodes


from typing import Optional
class Solution:

    values = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:    

        if node == None:
            return node
        elif len(node.neighbors) == 0:
            return Node(node.val)

        self.values = {}

        self.bfs(node)

        nodes = [Node(i+1) for i in range(len(self.values))]

        for i, neighbors in self.values.items():
            nodes[i-1].neighbors = [nodes[j - 1] for j in neighbors]

        return nodes[0]


    def bfs(self, node: Optional['Node']):
        if node.val:
            for neighbor in node.neighbors:
                try:
                    self.values[node.val].add(neighbor.val)
                except KeyError:
                    self.values[node.val] = set()
                    self.values[node.val].add(neighbor.val)

        for neighbor in node.neighbors:
            if neighbor.val in self.values:
                continue
            else:
                self.bfs(neighbor)
            
                
        

        


adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
graph = create_graph(adj_list)


s = Solution()
clone = s.cloneGraph(graph[0])

print(clone)

s.cloneGraph(Node(0))