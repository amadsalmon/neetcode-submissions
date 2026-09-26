class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(row,col) -> None:
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            _dfs(row-1,col)
            _dfs(row+1,col)
            _dfs(row, col-1)
            _dfs(row, col+1)

        island_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island_count += 1
                    _dfs(row, col)

        return island_count