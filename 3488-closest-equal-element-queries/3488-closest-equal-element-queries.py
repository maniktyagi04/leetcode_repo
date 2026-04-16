from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Store the list of indices for each unique value
        indices = defaultdict(list)
        for i, val in enumerate(nums):
            indices[val].append(i)
            
        # Precompute the answer for every index
        ans = [-1] * n
        
        for val, idx_list in indices.items():
            k = len(idx_list)
            # If a number appears only once, it remains -1
            if k < 2:
                continue
                
            for j in range(k):
                # Calculate distance to the left identical neighbor
                if j > 0:
                    left_dist = idx_list[j] - idx_list[j-1]
                else:
                    # Circular distance between first and last occurrence
                    left_dist = idx_list[0] + n - idx_list[-1]
                    
                # Calculate distance to the right identical neighbor
                if j < k - 1:
                    right_dist = idx_list[j+1] - idx_list[j]
                else:
                    # Circular distance between last and first occurrence
                    right_dist = idx_list[0] + n - idx_list[-1]
                    
                ans[idx_list[j]] = min(left_dist, right_dist)
                
        # Fetch the precomputed answer for each query
        return [ans[q] for q in queries]