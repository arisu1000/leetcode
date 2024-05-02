#https://leetcode.com/problems/min-stack

class MinStack:
    value = []

    def __init__(self):
        self.value = []    

    def push(self, val: int) -> None:
        self.value.append(val)

    def pop(self) -> None:
        self.value.pop()
        

    def top(self) -> int:
        return self.value[len(self.value) - 1]

    def getMin(self) -> int:
        return min(self.value)




# Your MinStack object will be instantiated and called as such:
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin(), -3); # return -3
minStack.pop();
print(minStack.top(), 0);    # return 0
print(minStack.getMin(), -2); # return -2

minStack = MinStack()
minStack.push(-1)
print(minStack.top(), -1)
print(minStack.getMin(), -1)