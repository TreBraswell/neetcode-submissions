class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if self.s:
            m = min(self.s[-1][1],val)
            self.s.append((val,m))
        else:
            self.s.append((val,val))

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        return self.s[-1][1]
