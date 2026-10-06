class Solution:
    """
    Second solution: iterate left to right
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                popped = stack.pop()
                i_popped = popped[1]
                res[i_popped] = i - i_popped
            
            stack.append((t,i))

        return res


    """
    First solution I came up with: iterate right to left
    """
    def dailyTemperatures_left_to_right(self, temperatures: List[int]) -> List[int]:
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
