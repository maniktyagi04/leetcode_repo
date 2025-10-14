class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def is_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for i in range(n - 2 * k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True

        return False
