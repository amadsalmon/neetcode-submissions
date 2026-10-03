class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two pass binary search
        # Each binary search is O(log N).
        # First pass on the m rows: log m
        # Second pass on a specific row of size n: log n
        # Total time complexity: log m + log n = O(log m * n) 
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        row = None
        col = None

        # First find at which row the target could be, by comparing the row's head
        left, right = 0, m-1
        while left <= right:
            row = (right + left) // 2
            if target < matrix[row][0] :
                row = row - 1
                right = row
            elif matrix[row][0] < target < matrix[row][-1]:
                break
            elif matrix[row][-1] < target:
                row = row + 1
                left = row
            else:
                return True  
        
        if row not in range(len(matrix)): return False

        # Then find within the row
        left, right = 0, n-1
        while left <= right:
            col = (right + left) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] == target:
                return True
        
        return False
        
