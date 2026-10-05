class Solution:
    def trap(self, height: List[int]) -> int:
        if 0 <= len(height) <= 2:
            # Can't trap any water if we don't have at least 3 tiles
            return 0

        # Find maxes at each i: (maxOnLeftOfI, maxOnRightOfI)
        maxes = [[0, 0] for _ in range(len(height))]
        lastMax = 0
        for i, h in enumerate(height):
            # Going left to right
            maxes[i][0] = lastMax
            if h > lastMax: lastMax = h
        lastMax = 0
        for i, h in reversed(list(enumerate(height))):
            # Now going right to left
            maxes[i][1] = lastMax
            if h > lastMax: lastMax = h

        # Now calculate water at each index
        total = 0
        for i, h in enumerate(height):
            water_capacity = min(maxes[i][0], maxes[i][1]) - h
            water_capacity = max(water_capacity, 0)
            total += water_capacity

        return total
        
