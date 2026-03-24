from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        
        # Initialize the result matrix with 0s
        p = [[0] * m for _ in range(n)]
        
        # Pass 1: Calculate prefix products
        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                # Update prefix product for the next element
                pref = (pref * (grid[i][j] % MOD)) % MOD
                
        # Pass 2: Calculate suffix products and multiply with prefixes
        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % MOD
                # Update suffix product for the preceding element
                suff = (suff * (grid[i][j] % MOD)) % MOD
                
        return p