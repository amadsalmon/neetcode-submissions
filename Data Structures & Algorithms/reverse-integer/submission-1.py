class Solution:
    def reverse(self, x: int) -> int:


        is_negative = False
        
        s = str(x)
        if x < 0:
            is_negative = True
            s = s[1:]

        n = len(s)
        summed = 0

        for i in range(n):
            summed += int(s[i]) * 10**i
        
        summed = summed if not is_negative else summed * -1

        if -2**31 <= summed <= 2**31 - 1:
            return summed
        else: 
            return 0

