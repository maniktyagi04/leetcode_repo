from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                direct_dist = abs(i - startIndex)
                
                wrap_dist = n - direct_dist
                
                shortest_path = min(direct_dist, wrap_dist)
                
                min_distance = min(min_distance, shortest_path)
                
        return min_distance if min_distance != float('inf') else -1