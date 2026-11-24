class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        This optimal solution is similar to 'Koko eating Bananas'.
        
        Complexity: time O(N * log N), space O(1)
        """
        
        def check(boatCapacity: int) -> bool:  # O(N)
            daysRequired = 1
            currentLoad = 0

            for w in weights:
                if currentLoad + w <= boatCapacity: 
                    currentLoad += w
                else:
                    daysRequired += 1
                    currentLoad = w

            return daysRequired <= days
        

        # We perform binary search to find the lowest valid boat capacity
        low = max(weights)  # O(N) - lowest boat capacity
        high = sum(weights)  # O(N) - highest boat capacity
        last_valid = -1
        
        while low <= high:  # O(log N)
            mid = (high + low) // 2
            if check(mid):  # O(N)
                high = mid - 1
                last_valid = mid
            else:
                low = mid + 1

        return last_valid