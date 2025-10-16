class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for num in nums:
            cnt[(num % value + value) % value] += 1

        mex = 0
        while True:
            r = mex % value
            if cnt[r] == 0:
                return mex
            cnt[r] -= 1
            mex += 1

        