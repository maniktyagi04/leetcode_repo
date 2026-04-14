from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()
        

        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)
            
        n = len(robot)

        dp = [0] + [float('inf')] * n
        

        for f in factory_positions:

            for i in range(n, 0, -1):
                dp[i] = min(dp[i], dp[i - 1] + abs(robot[i - 1] - f))
                
        return dp[n]