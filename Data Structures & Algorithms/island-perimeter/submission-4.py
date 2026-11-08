class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def findFirstLandTile(grid: List[List[int]]):
            r = 0
            while r in range(R):
                c = 0
                while c in range(C):
                    if grid[r][c] == 1:
                        return (r, c)
                    c += 1
                r += 1
            return (-1,-1)
        
        def dfs(r: int, c: int) -> int:
            if r not in range(R):
                return 1
            if c not in range(C):
                return 1
            if grid[r][c] == -1:
                return 0
            elif grid[r][c] == 0:
                return 1
            elif grid[r][c] == 1:
                # Mark as visited
                grid[r][c] = -1
                return (dfs(r-1, c) + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1))
            
            return 0

        r,c = findFirstLandTile(grid)
        return dfs(r, c) if (r, c) != (-1, -1) else 0
