#https://leetcode.com/problems/generate-parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:      

        def backtrack(current, open_count, close_count):  
            # If the current string has used all n pairs of parentheses
            if len(current) == 2*n:
                result.append(current)
                return
        
            # If we can still add an opening parenthesis
            if open_count < n :
                backtrack(current +"(", open_count + 1, close_count)
            
            # If we can still add a closing parenthesis
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)


        result = []
        backtrack("", 0, 0) # Start with an empty string and no parentheses used
        return result


s = Solution()
print(s.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

print(s.generateParenthesis(1), ["()"])
print(s.generateParenthesis(4), ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])