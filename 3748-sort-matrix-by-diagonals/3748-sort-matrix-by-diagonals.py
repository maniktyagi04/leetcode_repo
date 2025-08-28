from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Helper function to collect, sort, and place back a diagonal
        def process_diagonal(r: int, c: int, reverse: bool) -> None:
            res = []
            i, j = r, c
            while i < n and j < n:
                res.append(grid[i][j])
                i += 1
                j += 1

            res.sort(reverse=reverse)  # reverse=True → non-increasing, False → non-decreasing

            i, j = r, c
            for val in res:
                grid[i][j] = val
                i += 1
                j += 1
        for i in range(n):
            process_diagonal(i, 0, reverse=True)

        for j in range(1, n):
            process_diagonal(0, j, reverse=False)

        return grid
