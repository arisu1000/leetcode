from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        n = len(intervals)

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(n):
            if end < intervals[i][0]:
                result.append([start, end])
                start = intervals[i][0]
            
            if end < intervals[i][1]:
                end = intervals[i][1]

        result.append([start, end])
        
        return result


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[[1,4],[4,5]]]))
