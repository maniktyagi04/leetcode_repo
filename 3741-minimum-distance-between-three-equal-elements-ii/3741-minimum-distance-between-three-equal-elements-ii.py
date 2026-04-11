class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        n = len(nums)

        last1 = [-1] * (n + 1)
        last2 = [-1] * (n + 1)
        
        min_diff = float('inf')
        
        for i, num in enumerate(nums):

            if last2[num] != -1:
                min_diff = min(min_diff, i - last2[num])
            
            last2[num] = last1[num]
            last1[num] = i
            
        return min_diff * 2 if min_diff != float('inf') else -1