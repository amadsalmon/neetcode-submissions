class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
            if i != n-i-1:                
                sum += mat[n-i-1][i] 
        return sum
