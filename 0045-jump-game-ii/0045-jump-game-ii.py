class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        longest=0
        curr=0

        for i in range(len(nums)-1):
            longest=max(longest, i+nums[i])

            if i==curr:
                jumps+=1
                curr=longest
        return jumps