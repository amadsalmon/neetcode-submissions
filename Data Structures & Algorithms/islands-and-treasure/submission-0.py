from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        s = deque()

        for row in range(M):
            for col in range(N):
                if grid[row][col] == 0:
                    s.append((row, col))

        def bfs(r: int, c: int, prev_neighbour_value: int) -> None:
            if (r not in range(M)) or (c not in range(N)):
                return
            if grid[r][c] != 2147483647:
                return

            grid[r][c] = prev_neighbour_value + 1

            s.append((r, c))

        while s:
            r, c = s.popleft()
            for dr, dc in [(0,1), (1,0), (-1, 0), (0, -1)]:
                bfs(r + dr, c + dc, grid[r][c])
            
        return