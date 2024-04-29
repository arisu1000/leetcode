#https://leetcode.com/problems/merge-intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                if intervals[i][1] > end:
                    end = intervals[i][1]
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        ans.append([start, end])

        return ans


s = Solution()
print(s.merge([[1,4],[2,3]]), [[1,4]])
print(s.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
print(s.merge([[1,4],[4,5]]), [[1,5]])
