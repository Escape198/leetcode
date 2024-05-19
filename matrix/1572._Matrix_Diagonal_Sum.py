class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[i][n - 1 - i]

        if n % 2 == 1:
            diagonal_sum -= mat[n // 2][n // 2]

        return diagonal_sum
