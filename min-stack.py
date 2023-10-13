class MinStack:

    def __init__(self):
        self.arr = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.stack or self.stack[-1] >= val:
            self.stack.append(val)
    

        

    def pop(self) -> None:
     
        val = self.arr.pop()
        if val == self.stack[-1]:
            self.stack.pop()
        

    def top(self) -> int:
        
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()