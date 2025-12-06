class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from collections import deque
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * (n + 1)      
        prefix = [0] * (n + 1)   
        
        dp[0] = 1
        prefix[0] = 1
        
        minQ = deque()  
        maxQ = deque()  
        
        l = 0
        for r in range(n):

            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            minQ.append(nums[r])
            

            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            maxQ.append(nums[r])
            

            while maxQ[0] - minQ[0] > k:
                if minQ[0] == nums[l]:
                    minQ.popleft()
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                l += 1
            

            if l > 0:
                dp[r+1] = (prefix[r] - prefix[l-1]) % MOD
            else:
                dp[r+1] = prefix[r] % MOD
            
            prefix[r+1] = (prefix[r] + dp[r+1]) % MOD
        
        return dp[n] % MOD

        