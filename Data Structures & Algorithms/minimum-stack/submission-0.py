class MinStack:

    def __init__(self):
        self.core_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) > 0:
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)
        else:
            self.min_stack.append(val)
        self.core_stack.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()
        return self.core_stack.pop()

    def top(self) -> int:
        """No need to empty-check: 'pop, top and getMin will always be called on non-empty stacks.'"""
        return self.core_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
