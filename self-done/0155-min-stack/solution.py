class MinStack:

    def __init__(self):
        self.values = []
        self.minValues = [float('inf')]

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.minValues or val <= self.minValues[-1]:
            self.minValues.append(val)

    def pop(self) -> None:
        val = self.values.pop()
        if val == self.minValues[-1]:
            self.minValues.pop()
        return val

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minValues[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
