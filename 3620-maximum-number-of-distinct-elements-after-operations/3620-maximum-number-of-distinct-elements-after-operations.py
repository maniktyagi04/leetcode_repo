from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        intervals = [(x - k, x + k) for x in nums]
        intervals.sort(key=lambda t: t[1])
        last = -10**30
        cnt = 0
        for l, r in intervals:
            x = max(last + 1, l)
            if x <= r:
                cnt += 1
                last = x
        return cnt

        