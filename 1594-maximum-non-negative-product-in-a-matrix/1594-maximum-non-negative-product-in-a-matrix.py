from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Initialize DP tables to store max and min products up to each cell
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # Base case: top-left corner
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Pre-fill the first column (can only come from above)
        for i in range(1, m):
            max_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            min_dp[i][0] = min_dp[i-1][0] * grid[i][0]
            
        # Pre-fill the first row (can only come from the left)
        for j in range(1, n):
            max_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            min_dp[0][j] = min_dp[0][j-1] * grid[0][j]
            
        # Fill the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                # The 4 possible products coming from the top or left
                p1 = max_dp[i-1][j] * val
                p2 = min_dp[i-1][j] * val
                p3 = max_dp[i][j-1] * val
                p4 = min_dp[i][j-1] * val
                
                # Update max and min for the current cell
                max_dp[i][j] = max(p1, p2, p3, p4)
                min_dp[i][j] = min(p1, p2, p3, p4)
                
        ans = max_dp[-1][-1]
        
        # Return the modulo result if non-negative, else -1
        return ans % MOD if ans >= 0 else -1
        