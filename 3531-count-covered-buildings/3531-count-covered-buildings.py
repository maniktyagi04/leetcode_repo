from typing import List
import collections

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Precompute min and max columns for each row, and min and max rows for each column
        row_min = collections.defaultdict(lambda: 10**9)
        row_max = collections.defaultdict(lambda: -10**9)
        col_min = collections.defaultdict(lambda: 10**9)
        col_max = collections.defaultdict(lambda: -10**9)

        for x, y in buildings:
            if y < row_min[x]: row_min[x] = y
            if y > row_max[x]: row_max[x] = y
            if x < col_min[y]: col_min[y] = x
            if x > col_max[y]: col_max[y] = x

        ans = 0
        for x, y in buildings:
            # left and right exist in same row?
            has_left = row_min[x] < y
            has_right = row_max[x] > y
            # above and below exist in same column?
            has_above = col_min[y] < x
            has_below = col_max[y] > x

            if has_left and has_right and has_above and has_below:
                ans += 1

        return ans
