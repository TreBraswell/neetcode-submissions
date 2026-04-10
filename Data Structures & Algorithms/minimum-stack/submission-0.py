class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            val_min = self.min_stack[len(self.min_stack)-1]
            val = min(val_min,val)
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]


    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]
