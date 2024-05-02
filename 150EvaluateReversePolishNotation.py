#https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List

import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                
                if tokens[i] == "+":
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                elif tokens[i] == "/":
                    stack.append(math.trunc(first / second))
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()



s = Solution()
print(s.evalRPN(["2","1","+","3","*"]), 9)
print(s.evalRPN(["4","13","5","/","+"]), 6)
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
