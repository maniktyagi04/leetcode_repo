from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        total_sum = sum(row_sums)
        
        # Map value -> list of row indices and value -> list of col indices
        val_to_rows = defaultdict(list)
        val_to_cols = defaultdict(list)
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                val_to_rows[val].append(r)
                val_to_cols[val].append(c)
        
        # Sort indices for binary search
        for val in val_to_rows:
            val_to_rows[val].sort()
        for val in val_to_cols:
            val_to_cols[val].sort()

        def exists_in_range(val, index_list, start, end):
            if val not in index_list: return False
            lst = index_list[val]
            i = bisect_left(lst, start)
            return i < len(lst) and lst[i] <= end

        def check_discount(target_diff, is_horizontal, cut_idx, section_is_first):
            if target_diff == 0: return True
            if target_diff < 0: return False
            
            if is_horizontal:
                r_start, r_end = (0, cut_idx) if section_is_first else (cut_idx + 1, m - 1)
                num_rows = r_end - r_start + 1
                
                if num_rows > 1 and n > 1:
                    # Check if target_diff exists in rows [r_start, r_end]
                    return exists_in_range(target_diff, val_to_rows, r_start, r_end)
                elif num_rows == 1:
                    return grid[r_start][0] == target_diff or grid[r_start][n-1] == target_diff
                elif n == 1:
                    return grid[r_start][0] == target_diff or grid[r_end][0] == target_diff
            else:
                c_start, c_end = (0, cut_idx) if section_is_first else (cut_idx + 1, n - 1)
                num_cols = c_end - c_start + 1
                
                if num_cols > 1 and m > 1:
                    # Check if target_diff exists in columns [c_start, c_end]
                    return exists_in_range(target_diff, val_to_cols, c_start, c_end)
                elif num_cols == 1:
                    return grid[0][c_start] == target_diff or grid[m-1][c_start] == target_diff
                elif m == 1:
                    return grid[0][c_start] == target_diff or grid[0][c_end] == target_diff
            return False

        # Try Horizontal Cuts
        curr_top = 0
        for i in range(m - 1):
            curr_top += row_sums[i]
            other = total_sum - curr_top
            if check_discount(curr_top - other, True, i, True): return True
            if check_discount(other - curr_top, True, i, False): return True

        # Try Vertical Cuts
        curr_left = 0
        for j in range(n - 1):
            curr_left += col_sums[j]
            other = total_sum - curr_left
            if check_discount(curr_left - other, False, j, True): return True
            if check_discount(other - curr_left, False, j, False): return True

        return False