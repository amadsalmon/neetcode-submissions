class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        is_negative = False
        s = str(x)
        if x < 0:
            is_negative = True
            s = s[1:]

        n = len(s)
        summed = 0

        for i in range(n):
            summed += int(s[i]) * 10**i
            if not (MIN <= summed <= MAX):
                return 0
        
        return summed if not is_negative else summed * -1

