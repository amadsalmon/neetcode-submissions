class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def _getAreaOfIsland(row: int, col: int) -> int:
            if row not in range(len(grid)) or col not in range(len(grid[0])):
                return 0

            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            # Explore top, right, bottom, left
            return (
                1 +
                _getAreaOfIsland(row - 1, col) +
                _getAreaOfIsland(row, col + 1) +
                _getAreaOfIsland(row + 1, col) +
                _getAreaOfIsland(row, col - 1)
            )
        
        maxArea = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    maxArea = max(
                        _getAreaOfIsland(row, col), 
                        maxArea
                    )
        
        return maxArea
                    