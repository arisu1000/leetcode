#https://leetcode.com/problems/minimum-genetic-mutation

from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank_set = set(bank)
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            gene, level = queue.popleft()

            if gene == endGene:
                return level
            
            for i in range(8):
                for c in 'ACGT':
                    neighbor = gene[:i] + c + gene[i+1:]
                    if neighbor not in visited and neighbor in bank_set:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        return -1

    
s = Solution()


startGene = "AACCGGTT"
endGene = "AACCGCTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(s.minMutation(startGene, endGene, bank), 2)



startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(s.minMutation(startGene, endGene, bank), 2)


startGene = "AACCTTGG"
endGene = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
print(s.minMutation(startGene, endGene, bank), -1)

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT",
        "AACCGATA",
        "AAACGATA",
        "AAACGGTA"]
print(s.minMutation(startGene, endGene, bank), 4)




startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]

print(s.minMutation(startGene, endGene, bank), 1)

