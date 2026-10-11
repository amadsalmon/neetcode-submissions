def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Build trust matrix
        trust_matrix = [[0] * n for _ in range(n)]
        for [truster, trusted] in trust:
            trust_matrix[trusted-1][truster-1] = 1
        printMatrix(trust_matrix)

        def trusts_nobody(i):
            for j in range(n):
                if trust_matrix[j][i]:
                    return False
            return True
        
        def trusted_by_all(i):
            for j in range(n):
                if j != i and not trust_matrix[i][j]:
                    return False
            return True

        for i in range(n):
            if trusts_nobody(i) and trusted_by_all(i):
                return i + 1

        return -1
