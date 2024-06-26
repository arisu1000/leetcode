#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = []
        points.sort()
        
        i = 0
        start = points[0][0]
        end = points[0][1]
        while i < len(points):
            if start <= points[i][0] <= end:
                if points[i][1] <= end:
                    end = points[i][1]
            elif end < points[i][0]:
                ans.append([start, end])
                start = points[i][0]
                end = points[i][1]
            
            i += 1

        ans.append([start, end])

        return len(ans)


s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]), 2)
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]), 4)
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]), 2)