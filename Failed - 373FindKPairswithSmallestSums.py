# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

from typing import List

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        #최소 힙 초기화
        min_heap = []
        # 결과 배열
        result = []

        #힙에 초기 (i, 0) 위치의 쌍을 저장
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # k개의 쌍을 찾을 때까지 힙에서 최소합 쌍을 pop
        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # 다음 요소 추가 (i, j+1)
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

        return result





s = Solution()

print(s.kSmallestPairs([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])


print(s.kSmallestPairs([1,1,2], [1,2,3], 2), [[1,1],[1,1]])