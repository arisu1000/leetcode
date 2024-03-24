from typing import List

class Solution:
    # total_permutations = []
    selectStr = ''
    count = 0

    def getPermutation(self, n: int, k: int) -> str:
        list = [str(i) for i in range(1, n+1)]
        # print(list)

        self.makePermutation(list, [], k)
        return self.selectStr        

    def makePermutation(self, list, path, k):
        
        if len(list) == len(path):
            # self.total_permutations.append(path[:])
            self.count += 1
            # print(path)
            if self.count == k:
                self.selectStr = ''.join(path)

            return

        for i in range(len(list)):
            # if self.count == k:
            #     return
            if list[i] not in path:
                path.append(list[i])
                self.makePermutation(list, path, k)
                path.pop()

s = Solution()
# print(s.getPermutation(3, 3))
# print(s.getPermutation(4, 9))
print(s.getPermutation( 9, 305645))
