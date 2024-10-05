#https://leetcode.com/problems/generate-parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        result = set()

        def backtrack(parenthesis, i):    
            if i == n:
                result.add(parenthesis)
                return
            
            backtrack("("+parenthesis+")", i+1)
            backtrack(parenthesis+"()", i+1)
            backtrack("()"+parenthesis, i+1)
        
        if n == 0:
            return result

        backtrack("()", 1)

        return list(result)
    


s = Solution()
print(s.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

print(s.generateParenthesis(1), ["()"])