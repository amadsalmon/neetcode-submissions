class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
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


