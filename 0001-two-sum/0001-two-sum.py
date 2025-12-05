class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}

        for i,n in enumerate(nums):
            if target-n in temp:
                return [temp[target-n],i]
            
            temp[n]=i
        