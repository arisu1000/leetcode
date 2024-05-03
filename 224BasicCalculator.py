#https://leetcode.com/problems/basic-calculator


class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        # 괄호면 내부걸 처리한다. -> 최종 값은 숫자로 변경됨
        # 괄호안에 괄호가 있는 경우 -> 괄호 처리에 대한 건 별도의 함수를 만들어서 호출한다.
        # + 면 양쪽을 더한다.
        # - 면 계산한다. 앞에 숫자가 없으면 뒤에 값을 -로 변환한다.
        # ' ' 공백은 건너뛴다.

        i = 0
        while i < len(s):
            if s[i] == "+":
                val, i = self.sum(s, i, stack.pop())
                stack.append(val)
            elif s[i] == "-":
                val, i = self.minus(s, i, stack)
                stack.append(val)
            elif s[i] == "(":
                val, i = self.bracket(s, i+1)
                stack.append(val)            
            elif s[i] == " ":
                i += 1
                continue
            else:
                val, i = self.getVal(s, i)
                stack.append(val)

        return stack.pop()
    
    def sum(self, s: str, i: int, num1: int) -> (int, int):
        nextVal = 0

        while s[i+1] == " ":
            i += 1

        if s[i+1] == "(":
            nextVal, i = self.bracket(s, i+2)
        else:
            i += 1
            while s[i] == " ":
                i += 1
                continue
            nextVal, i = self.getVal(s, i)
        
        return num1 + nextVal, i
    
    def minus(self, s: str, i: int, stack: []) -> (int, int):
        nextVal = 0
        num1 = 0
        if len(stack) > 0:
            num1 = stack.pop()

        while s[i+1] == " ":
            i += 1
        
        if s[i+1] == "(":
            nextVal, i = self.bracket(s, i+2)
        else:
            i += 1
            while s[i] == " ":
                i += 1
                continue
            nextVal, i = self.getVal(s, i)
        
        return num1 - nextVal, i

    
    def bracket(self, s: str, i: int) -> (int, int):
        
        stack = []

        while i < len(s) and s[i] != ")":
            if s[i] == "+":
                val, i = self.sum(s, i, stack.pop())
                stack.append(val)
            elif s[i] == "-":
                val, i = self.minus(s, i, stack)
                stack.append(val)
            elif s[i] == " ":
                i += 1
                continue
            elif s[i] == "(":
                self.bracket(s, i + 1)
            else:
                while s[i] == " ":
                    i += 1
                    continue
                val, i = self.getVal(s, i)
                stack.append(val)

        return stack.pop(), i + 1
            
    def getVal(self, s: str, i: int) -> (int, int):
        numberLen = 0
        while i+numberLen < len(s) and s[i+numberLen].isdigit():
            numberLen += 1
        
        return int(s[i:i+numberLen]), i+numberLen

s = Solution()
print(s.calculate("- (3 + (4 + 5))"), -12)
print(s.calculate("-2+ 1"), -1)
print(s.calculate("1-(     -2)"), 3)
print(s.calculate("2147483647"), 2147483647)
print(s.calculate("1 + 1"), 2)
print(s.calculate(" 2-1 + 2 "), 3)
print(s.calculate("(1+(4+5+2)-3)+(6+8)"), 23)


# print(s.bracket("(1+(4+5+2)-3)+(6+8)", 4), 11)