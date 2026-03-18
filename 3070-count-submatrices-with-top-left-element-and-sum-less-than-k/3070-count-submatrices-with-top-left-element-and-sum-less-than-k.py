from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # Create a 2D array padded with an extra row and column of 0s
        # This prevents out-of-bounds errors when referencing i-1 or j-1
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                # Calculate the prefix sum for the current cell
                prefix[i+1][j+1] = (
                    grid[i][j] 
                    + prefix[i][j+1]     # Sum of elements above
                    + prefix[i+1][j]     # Sum of elements to the left
                    - prefix[i][j]       # Subtract the overlapping top-left section
                )
                
                # Check if the sum of the submatrix (from 0,0 to i,j) is within the limit k
                if prefix[i+1][j+1] <= k:
                    count += 1
                    
        return count