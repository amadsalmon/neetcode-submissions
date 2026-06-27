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
        
        def getSubBox(board: List[List[str]], i: int, j: int)-> List[str]:
            subbox_as_line = []
            for y in range(j, j+3):
                for x in range(i, i+3):
                    subbox_as_line.append(board[y][x])
            return subbox_as_line
                
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
        for i in range(0, 3):
            for j in range(0, 3):
                subbox = getSubBox(board, i*3, j*3)
                if not isValidLine(subbox):
                    return False

        return True
