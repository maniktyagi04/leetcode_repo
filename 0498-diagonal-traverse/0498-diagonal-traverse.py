from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        # Loop over all possible diagonals
        for d in range(m + n - 1):
            intermediate = []
            
            # Determine starting point of this diagonal
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            
            # Collect elements along this diagonal
            while r < m and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # Reverse every alternate diagonal to get zigzag pattern
            if d % 2 == 0:
                intermediate.reverse()
            
            result.extend(intermediate)
        
        return result
