from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG = -10**18

        # dp[t][state]
        # state: 0 = neutral, 1 = holding long, 2 = holding short
        dp = [[NEG, NEG, NEG] for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            new_dp = [row[:] for row in dp]

            for t in range(k + 1):
                # From neutral
                if dp[t][0] != NEG:
                    # open long
                    new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)
                    # open short
                    new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)

                # Close long
                if t < k and dp[t][1] != NEG:
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)

                # Close short
                if t < k and dp[t][2] != NEG:
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)

            dp = new_dp

        return max(dp[t][0] for t in range(k + 1))

        