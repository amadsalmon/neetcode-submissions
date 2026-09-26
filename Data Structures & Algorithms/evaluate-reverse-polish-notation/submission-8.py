class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []
        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[t](left, right))
            else:
                stack.append(int(t))
        
        return stack.pop()
            
                
