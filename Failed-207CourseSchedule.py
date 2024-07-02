#https://leetcode.com/problems/course-schedule

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        matrix = []
        for i in range(numCourses):
            matrix.append([0 for j in range(numCourses)])

        for prerequisit in prerequisites:
            matrix[prerequisit[0]][prerequisit[1]] += 1
        
        count = 0
        def check(i, j) -> bool:
            nonlocal count

            if matrix[i][j] == 0:
                if count <= numCourses:
                    return True
                else:
                    return False
            else:
                count += 1
                if count > numCourses:
                    return False
                else:
                    check(j,i)
                    if count <= numCourses:
                        return True
                    else:
                        return False
                   
        result = False
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 1:
                    result = check(row,col)
                    
        if result == True and count <= numCourses:
            return True
        else:
            return False

s = Solution()
print(s.canFinish(3, [[1,0],[0,2],[2,1]]), False)
print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]), False)
print(s.canFinish(2, [[1,0]]), True)
print(s.canFinish(2, [[1,0],[0,1]]), False)
print(s.canFinish(3, [[1,0]]), True)
print(s.canFinish(3, [[0,1],[0,2],[1,2]]), True)

