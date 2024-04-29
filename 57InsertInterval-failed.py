#https://leetcode.com/problems/insert-interval

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]


        ans = []

        start = -1
        end = -1
        findNewInterval = False
        for i in range(len(intervals)):

            if findNewInterval == True:
                ans.append(intervals[i])
                continue
            
            if newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
                start = newInterval[0]
                end = newInterval[1]
            if newInterval[0] < intervals[i][0]:
                start = newInterval[0]
            elif newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                start = intervals[i][0]
            
            if newInterval[1] < intervals[i][0]:
                end = newInterval[1]
            elif newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
                end = intervals[i][1]           

            if start != -1 and end != -1:
                findNewInterval = True
                ans.append([start, end])

            # try:
            #     if newInterval[0] < intervals[i][0]:
            #         start = newInterval[0] 
            #     elif (newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]) or (newInterval[0] > intervals[i][1] and newInterval[0] < intervals[i+1][0]):
            #         start = intervals[i][0]
            # except IndexError:
            #     if newInterval[0] > intervals[i][1]:
            #         ans.append(intervals[i])
            #         start = newInterval[0]
            #         end = newInterval[1]

            # try:            
            #     if newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
            #         end = intervals[i][1]
            #     elif newInterval[1] < intervals[i+1][0]:
            #         end = newInterval[1]
            # except IndexError:
            #     if newInterval[1] >= intervals[i][1]:
            #         end = newInterval[1]
            #     else:
            #         break
                
            # if start == -1:
            #     ans.append(intervals[i])
            # elif start > -1 and end == -1:
            #     continue
            # elif start > -1 and end > -1:
            #     findNewInterval = True
            #     ans.append([start, end])


        return ans


s = Solution()

print(s.insert([[1,5]], [0,3]), [[0,5]])
print(s.insert([[1,5]], [6,8]), [[1,5],[6,8]])
print(s.insert([[1,5]], [2,7]), [[1,7]])
print(s.insert([], [5,7]), [[5,7]])
print(s.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])

