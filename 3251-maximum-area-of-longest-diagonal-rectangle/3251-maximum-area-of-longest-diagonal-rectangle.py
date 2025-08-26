from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_sq = 0  # store diagonal squared
        max_area = 0
        
        for length, width in dimensions:
            diagonal_sq = length * length + width * width  # diagonal squared
            area = length * width
            
            # If this diagonal is longer, or same but larger area, update
            if diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = diagonal_sq
                max_area = area
            elif diagonal_sq == max_diagonal_sq and area > max_area:
                max_area = area
        
        return max_area
