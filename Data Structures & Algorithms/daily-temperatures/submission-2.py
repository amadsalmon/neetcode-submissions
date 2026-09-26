class Solution:
    def dailyTemperatures_brute_force(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            j = i + 1
            while j < len(temperatures):
                if temperatures[j]>t:
                    res[i]= j - i
                    break
                j += 1  
        return res
    
    def dailyTemperatures_try(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            if s: 
                if s[-1] > t:
                    res[i] = 1
                else:
                    count = 0
                    while True:
                        if s[-1]<=t:
                            s.pop()
                            count += 1
                        else:
                            count += 1
                            break
                        if not s: 
                            count = 0 
                            break
                    res[i]= count

            s.append(t)
        
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # holds indices of days still waiting for a warmer day

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res