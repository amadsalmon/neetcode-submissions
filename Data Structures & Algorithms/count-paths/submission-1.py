class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = 1

        def dfs(row: int, col: int):
            if row < 0 or row > m or col < 0 or col > n:
                return 0
            if matrix[row][col] != 0: return matrix[row][col]
            matrix[row][col] += dfs(row, col - 1) + dfs(row - 1, col)
            return matrix[row][col]

        return dfs(m-1, n-1)
        