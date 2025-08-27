from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0]) if grid else 0
        if n == 0 or m == 0:
            return 0

        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        orders = [
            (range(n), range(m - 1, -1, -1)),
            (range(n - 1, -1, -1), range(m - 1, -1, -1)),
            (range(n - 1, -1, -1), range(m)),
            (range(n), range(m))
        ]

        def make():
            return [[[0] * m for _ in range(n)] for __ in range(4)]

        A1, A2, A0 = make(), make(), make()

        for d in range(4):
            di, dj = dirs[d]
            oi, oj = orders[d]
            for i in oi:
                for j in oj:
                    ni, nj = i + di, j + dj
                    inside = 0 <= ni < n and 0 <= nj < m
                    if grid[i][j] == 2:
                        A2[d][i][j] = 1 + (A0[d][ni][nj] if inside and grid[ni][nj] == 0 else 0)
                    else:
                        A2[d][i][j] = 0
                    if grid[i][j] == 0:
                        A0[d][i][j] = 1 + (A2[d][ni][nj] if inside and grid[ni][nj] == 2 else 0)
                    else:
                        A0[d][i][j] = 0
                    if grid[i][j] == 1:
                        A1[d][i][j] = 1 + (A2[d][ni][nj] if inside and grid[ni][nj] == 2 else 0)
                    else:
                        A1[d][i][j] = 0

        B2, B0 = make(), make()
        for d in range(4):
            di, dj = dirs[d]
            cw = (d + 1) & 3
            cdi, cdj = dirs[cw]
            oi, oj = orders[d]
            for i in oi:
                for j in oj:
                    if grid[i][j] == 2:
                        best = 1
                        si, sj = i + di, j + dj
                        if 0 <= si < n and 0 <= sj < m and grid[si][sj] == 0:
                            best = max(best, 1 + B0[d][si][sj])
                        ti, tj = i + cdi, j + cdj
                        if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 0:
                            best = max(best, 1 + A0[cw][ti][tj])
                        B2[d][i][j] = best
                    else:
                        B2[d][i][j] = 0
                    if grid[i][j] == 0:
                        best = 1
                        si, sj = i + di, j + dj
                        if 0 <= si < n and 0 <= sj < m and grid[si][sj] == 2:
                            best = max(best, 1 + B2[d][si][sj])
                        ti, tj = i + cdi, j + cdj
                        if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 2:
                            best = max(best, 1 + A2[cw][ti][tj])
                        B0[d][i][j] = best
                    else:
                        B0[d][i][j] = 0

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                for d in range(4):
                    ans = max(ans, A1[d][i][j])
                    di, dj = dirs[d]
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                        ans = max(ans, 1 + B2[d][ni][nj])

        return ans
