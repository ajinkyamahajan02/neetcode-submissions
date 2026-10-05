class MinStack:

    def __init__(self):
        self.stk = []
        

    def push(self, val: int) -> None:
        return self.stk.append(val)
        

    def pop(self) -> None:
        return self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        tmp = []
        mini = self.stk[-1]

        while len(self.stk):
            mini = min(mini, stk[-1])
            tmp.append(stk.pop())

        while len(tmp):
            self.stk.append(tmp.pop())
        return mini