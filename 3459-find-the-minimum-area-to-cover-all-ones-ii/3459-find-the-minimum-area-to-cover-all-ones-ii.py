from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Collect all 1-cells once
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        # If no 1s: we still must place 3 non-overlapping rectangles with non-zero area.
        # Any guillotine layout with 3 regions gives cost 1+1+1 = 3.
        if not ones:
            return 3

        INF = 10**18

        # area of tight bbox of ones inside region [r0,r1) x [c0,c1)
        # if region has no 1s => must place a 1x1 dummy rectangle there -> area = 1
        def area_region(r0: int, r1: int, c0: int, c1: int) -> int:
            minr, maxr = m, -1
            minc, maxc = n, -1
            found = False
            for i, j in ones:
                if r0 <= i < r1 and c0 <= j < c1:
                    found = True
                    if i < minr: minr = i
                    if i > maxr: maxr = i
                    if j < minc: minc = j
                    if j > maxc: maxc = j
            if not found:
                return 1  # dummy 1x1 rectangle in this region
            return (maxr - minr + 1) * (maxc - minc + 1)

        best = INF

        # 1) V|V: three vertical strips
        for c1 in range(1, n - 1):
            for c2 in range(c1 + 1, n):
                cost = (
                    area_region(0, m, 0, c1) +
                    area_region(0, m, c1, c2) +
                    area_region(0, m, c2, n)
                )
                if cost < best: best = cost

        # 2) H-H: three horizontal strips
        for r1 in range(1, m - 1):
            for r2 in range(r1 + 1, m):
                cost = (
                    area_region(0, r1, 0, n) +
                    area_region(r1, r2, 0, n) +
                    area_region(r2, m, 0, n)
                )
                if cost < best: best = cost

        # 3) V → LH: split left side horizontally
        for c in range(1, n):
            for r in range(1, m):
                cost = (
                    area_region(0, r, 0, c) +      # left-top
                    area_region(r, m, 0, c) +      # left-bottom
                    area_region(0, m, c, n)        # right
                )
                if cost < best: best = cost

        # 4) V → RH: split right side horizontally
        for c in range(1, n):
            for r in range(1, m):
                cost = (
                    area_region(0, m, 0, c) +      # left
                    area_region(0, r, c, n) +      # right-top
                    area_region(r, m, c, n)        # right-bottom
                )
                if cost < best: best = cost

        # 5) H → TV: split top side vertically
        for r in range(1, m):
            for c in range(1, n):
                cost = (
                    area_region(0, r, 0, c) +      # top-left
                    area_region(0, r, c, n) +      # top-right
                    area_region(r, m, 0, n)        # bottom
                )
                if cost < best: best = cost

        # 6) H → BV: split bottom side vertically
        for r in range(1, m):
            for c in range(1, n):
                cost = (
                    area_region(0, r, 0, n) +      # top
                    area_region(r, m, 0, c) +      # bottom-left
                    area_region(r, m, c, n)        # bottom-right
                )
                if cost < best: best = cost

        return best
