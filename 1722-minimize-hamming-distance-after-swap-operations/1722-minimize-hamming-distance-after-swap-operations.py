from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        # Initialize Disjoint Set Union (DSU) arrays
        parent = list(range(n))
        rank = [1] * n
        
        # DSU Find with path compression
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        # DSU Union by rank
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                
        # 1. Group indices into connected components
        for u, v in allowedSwaps:
            union(u, v)
            
        # 2. Gather all indices belonging to the same component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        hamming_distance = 0
        
        # 3. Calculate minimum Hamming distance per component
        for indices in components.values():
            # Count frequencies of available numbers in the 'source' for this component
            source_counts = Counter(source[i] for i in indices)
            
            for i in indices:
                # If we have a matching element available, pair it and decrement its count
                if source_counts[target[i]] > 0:
                    source_counts[target[i]] -= 1
                else:
                    # If no matching element is available in this component, it contributes to the distance
                    hamming_distance += 1
                    
        return hamming_distance