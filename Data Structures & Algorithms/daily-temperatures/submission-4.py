class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            current = temperatures[i]
            while stack and stack[-1][0] <= current:
                stack.pop()
            
            if stack:
                # Top of stack is now an element that has a higher temperature than current
                res[i] = stack[-1][1] - i 
            
            stack.append([temperatures[i], i])

        return res
