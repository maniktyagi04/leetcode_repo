from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Valid pair (if j >= i, j - i is positive; if j < i, it evaluates to < 0 and max() ignores it)
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # nums2[j] is too small, need a smaller nums1[i] to match
                i += 1
                
        return max_dist