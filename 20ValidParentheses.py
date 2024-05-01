#https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            try:
                if s[i] in ["(", "[", "{"]:
                    stack.append(s[i])
                elif s[i] == ")":
                    if stack.pop() != "(":
                        return False
                elif s[i] == "]":
                    if stack.pop() != "[":
                        return False
                elif s[i] == "}":
                    if stack.pop() != "{":
                        return False
            except:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
     

s = Solution()

print(s.isValid("()"), True)
print(s.isValid("()[]{}"), True)
print(s.isValid("(]"), False)
print(s.isValid("(){}}{"), False)
print(s.isValid("{[]}"), True)
print(s.isValid("([]){"), False)
print(s.isValid("[[[]"), False)