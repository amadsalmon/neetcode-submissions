from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        minutes = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0: return 0

        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for (drow, dcol) in [(-1,0), (0,-1), (1,0), (0,1)]:
                    nrow = row + drow
                    ncol = col + dcol
                    if nrow not in range(len(grid)) or ncol not in range(len(grid[0])) or grid[nrow][ncol] == 0:
                        continue
                    if grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh_oranges -= 1
                    if grid[nrow][ncol] == 2:
                        grid[nrow][ncol] = 3
                        queue.append((nrow, ncol))
            minutes += 1
            print(grid)

        if fresh_oranges > 0: return -1 
        
        return minutes 