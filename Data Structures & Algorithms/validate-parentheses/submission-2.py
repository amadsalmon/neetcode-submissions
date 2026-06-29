class Stack:
    def __init__(self):
        self.__storage = []
    
    def push(self, item):
        self.__storage.append(item)

    def peek(self):
        if self.isEmpty():
            return None
        return self.__storage[-1]

    def pop(self):
        if self.isEmpty():
            raise IndexError("Unable to pop from empty stack")
        return self.__storage.pop()
    
    def isEmpty(self):
        return len(self.__storage) == 0
    
OPENING_CHARS = set(['(', '[', '{'])
CLOSING_CHARS = set([')', ']', '}'])

CLOSER_TO_OPENER = {
    ')': '(',
    '}': '{',
    ']': '[',
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()

        for c in s:
            if c in OPENING_CHARS:
                stack.push(c)
            if c in CLOSING_CHARS:
                if stack.isEmpty():
                    return False
                opener_actual = stack.pop()
                opener_expectation = CLOSER_TO_OPENER[c]
                if opener_actual != opener_expectation:
                    return False
        
        if not stack.isEmpty():
            return False
        
        return True






        