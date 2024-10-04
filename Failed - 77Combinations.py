#https://leetcode.com/problems/combinations/description

from typing import List

class Solution:

    result = []
    k = 0
    n = 0

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            # If the combination is complete, add it to the result
            if len(path) == k:
                result.append(path[:])
                return
        
            # Explore each number from 'start' to 'n'
            for i in range(start, n+1):
                path.append(i)          # Add the number to the current combination
                backtrack(i + 1, path)  # Recur to explore further numbers
                path.pop()              # Backtrack and remove the last number
        
        result = []
        backtrack(1, [])
        return result


s = Solution()

print(s.combine(3, 3), [[1,2,3]])
print(s.combine(4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
print(s.combine(1, 1), [[1]])

