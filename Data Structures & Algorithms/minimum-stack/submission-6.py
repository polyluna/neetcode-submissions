class MinStack:

    def __init__(self):
        self.stack = []
        self.ms = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.ms) != 0 and self.ms[-1] < val:
            self.ms.append(self.ms[-1])
        else:
            self.ms.append(val)

    def pop(self) -> None:
        self.stack .pop()
        self.ms.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ms[-1]
