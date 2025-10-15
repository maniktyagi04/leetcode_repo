class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        inc = [1 if nums[i] < nums[i+1] else 0 for i in range(n-1)]
        pref = [0]*(len(inc)+1)
        for i, v in enumerate(inc):
            pref[i+1] = pref[i] + v

        def all_inc(start, k):
            return pref[start + k - 1] - pref[start] == k - 1

        def exists(k):
            if 2*k > n:
                return False
            last = n - 2*k
            for a in range(last + 1):
                if all_inc(a, k) and all_inc(a + k, k):
                    return True
            return False

        lo, hi, ans = 1, n//2, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if exists(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
