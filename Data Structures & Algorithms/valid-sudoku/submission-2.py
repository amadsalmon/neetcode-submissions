class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidLine(line: List[str]) -> bool:
            seen = [True] + [False] * 9
            for tile in line:
                if tile != '.':
                    if seen[int(tile)]:
                        return False
                    else:
                        seen[int(tile)] = True
            return True
                
        # Check rows
        for row in board:
            if not isValidLine(row):
                return False

        # Check columns
        for col_index in range(9):
            col = [row[col_index] for row in board]
            if not isValidLine(col):
                return False
        
        # Check each 3x3 subbox of the board
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[y][x] for y in range(j, j+3) for x in range(i, i+3)]
                if not isValidLine(box):
                    return False

        return True
