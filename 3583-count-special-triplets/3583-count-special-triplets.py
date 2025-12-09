class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        
        MOD = 10**9 + 7
        right = Counter(nums)  
        left = Counter()      
        
        ans = 0
        
        for j in range(len(nums)):
            right[nums[j]] -= 1    
            
            target = nums[j] * 2
            

            ans = (ans + left[target] * right[target]) % MOD
            
            left[nums[j]] += 1     
        
        return ans % MOD

        