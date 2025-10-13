class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0] * n
        
        if n==0:
            return 0
        if n==1:
            return nums[0]

        dp[0] = nums[0]     #sirf pehla ghar loot lo 
        dp[1] = max(nums[0], nums[1])    # dono me vo ghar loot lo jisme paisa jyada hai 

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

        
        