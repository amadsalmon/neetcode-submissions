class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: 
            return x
        
        low, high = 1, x // 2
        last_valid = -1

        while low <= high:
            mid = (high + low) // 2 
            current = mid * mid
            if current < x:
                last_valid = mid
                low = mid + 1
            elif current > x:
                high = mid - 1
            else:
                return mid

        return last_valid


