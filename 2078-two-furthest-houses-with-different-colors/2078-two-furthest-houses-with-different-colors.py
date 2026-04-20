from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # 1. Find the max distance from the first house (index 0)
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
                
        # 2. Find the max distance from the last house (index n-1)
        for i in range(0, n - 1):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, n - 1 - i)
                break
                
        return max_dist