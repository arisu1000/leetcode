from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        for i in range(n):
            tmp = []

            if i == 0:
                tmp = ["()"]

            while len(result) > 0:
                r = result.pop()
                
                r1 = "(" + r + ")"
                r2 = "()" + r
                r3 = r + "()"
                tmp.append(r1)
                tmp.append(r2)
                tmp.append(r3)

            result = tmp

        set_r = set(result)
        
        return list(set_r)

s = Solution()

print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
