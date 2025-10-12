class Solution:
    def climbStairs(self, n: int) -> int:

        dp=[-1]*(n+1)

        def helper(x):
            if x==1:
                return 1
            if x==2:
                return 2
            
            if x in dp:
                return dp[x]

            dp[x] = helper(x-1) + helper(x-2)
            return dp[x]

        return helper(n)


        