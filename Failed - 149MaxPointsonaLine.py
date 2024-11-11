# https://leetcode.com/problems/max-points-on-a-line

from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        points.sort()
        # 기울기를 계산한다.
        # 기울기대로 했을때 다음 포인트가 존재하는지 확인한다.

        def calDecade(a: List[int], b: List[int]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            
            return [dx, dy]


        maxCount = 0
        for i in range(0, len(points)):
            j = i + 1

            count = {}
            while j < len(points):
                decade = calDecade(points[i], points[j])
                j += 1

                key = 0
                if decade[0] != 0 and decade[1] != 0:
                    key = decade[0]/decade[1]
                else:
                    key = str(decade[0]) + str(decade[1])

                try:
                    count[key] += 1
                except KeyError:
                    count[key] = 2
            
            if len(count) > 0:
                key = max(count, key=count.get)
                maxCount = max(maxCount, count[key])

        return maxCount
    


s = Solution()

print(s.maxPoints([[1,1],[2,2],[3,3]]), 3)
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4)
