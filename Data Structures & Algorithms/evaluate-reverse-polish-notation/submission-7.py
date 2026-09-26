class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ('+', '-', '*', '/')
        for t in tokens:
            match t:
                case '+':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left + right)
                case '-':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left - right)
                case '*':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left * right)
                case '/':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left / right))
                case _:
                    stack.append(int(t))
        
        return stack.pop()
            
                
