class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])         
        
        def isCoastalTile(r: int, c: int) -> int:
            if r not in range(R) or c not in range(C): # Edges
                return 1
            elif grid[r][c] == 0:  # Sea tiles
                return 1
            return 0

        perimeter = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    for (dr, dc) in [(-1,0), (0,1), (1,0), (0,-1)]:
                        perimeter += isCoastalTile(r+dr, c+dc)
                    
        return perimeter
