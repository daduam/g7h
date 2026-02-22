from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        cols = []
        for cc in range(m):
            col = [matrix[rr][cc] for rr in range(n)]
            cols.append(col)
        return cols
