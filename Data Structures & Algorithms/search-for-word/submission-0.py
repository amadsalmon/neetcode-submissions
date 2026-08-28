class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for c in range(len(board[0])):
            for r in range(len(board)):
                if self.backtrack(board, word, r, c, 0, visited):
                    return True
        return False

    def backtrack(self, board, word, r, c, index, visited):
        if index == len(word):
            return True

        if not self.areCoordinatesInBoardBounds(board, r, c) or (r,c) in visited or board[r][c] != word[index]:
            return False

        visited.add((r,c))

        if (
            self.backtrack(board, word, r-1, c, index + 1, visited)
            or
            self.backtrack(board, word, r, c+1, index + 1, visited)
            or
            self.backtrack(board, word, r+1, c, index + 1, visited)
            or
            self.backtrack(board, word, r, c-1, index + 1, visited)
        ):
            return True
        
        visited.remove((r,c))

        return False
    
    def areCoordinatesInBoardBounds(self, board, r, c):
        return not (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]))



        