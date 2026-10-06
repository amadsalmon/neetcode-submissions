class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            current = temperatures[i]
            if len(stack) > 0:
                peeked = stack[-1]
                if peeked[0] > current:
                    res[i] = peeked[1] - i
                else:
                    while stack and stack[-1][0] <= current:
                        stack.pop()
                    
                    if stack:
                        # Top of stack is now an element that has a higher temperature than current
                        peeked = stack[-1]
                        res[i] = peeked[1] - i 
            
            stack.append([temperatures[i], i])

        return res
