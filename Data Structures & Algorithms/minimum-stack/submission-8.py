class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        return self.stk.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        return self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]