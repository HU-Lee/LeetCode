class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_min = set(min(matrix[i]) for i in range(m))
        col_max = set(
            max(matrix[j][i] for j in range(m))
            for i in range(n)
        )

        return list(row_min & col_max)