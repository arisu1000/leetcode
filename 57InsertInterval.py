from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        # n = len(intervals)
        # startInvervalIndex = -1
        # endInvervalIndex = -1
        # for i in range(n):
        #     if intervals[i][0] <= newInterval[0] and newInterval[0] <= intervals[i][1]:
        #         if startInvervalIndex == -1:
        #             startInvervalIndex = i
            
        #     if newInterval[1] <= intervals[i][1]:
        #         if endInvervalIndex == -1:
        #             endInvervalIndex = i

        # print(startInvervalIndex, endInvervalIndex)
        # mergeInterval = [intervals[startInvervalIndex][0], intervals[endInvervalIndex][1]]
        

        # for i in range(n):
        #     if i < startInvervalIndex or endInvervalIndex <= i:
        #         result.append(intervals[i])
        #     else:
        #         result.append(mergeInterval)

        return result


s = Solution()

print(s.insert([[1,3],[6,9]], [2,5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

