# https://leetcode.com/problems/ipo

from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 프로젝트 수 
        n = len(profits)

        # 프로젝트를 (capital, profit)쌍으로 묶어 정렬
        projects = sorted(zip(capital, profits), key=lambda x: x[0])

        # 최소 힙 초기화 (프로젝트를 자본 기준으로 정렬)
        min_heap = []
        for project in projects:
            heapq.heappush(min_heap, project)

        # 최대 힙 초기화 (현재 자본으로 시작할 수 있는 프로젝트 중 가장 높은 profit)
        max_heap = []

        for _ in range(k):
            # 현재 자본 w으로 시작할 수 있는 모든 프로젝트를 최대 힙으로 이동
            while min_heap and min_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -prof) # profit을 음수로 저장하여 최대 힙처럼 사용

            # 최대 힙에서 가장 높은 profit을 가진 프로젝트 선택
            if max_heap:
                w += -heapq.heappop(max_heap)
            else:
                # 더 이상 선택할 수 있는 프로젝트가 없으면 종료
                break

        return w
    
s = Solution()

print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1] ), 4)
print(s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2] ), 6)

