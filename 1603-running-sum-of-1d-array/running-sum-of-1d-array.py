class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        out=[0]*n
        sum=0
        for i in range(n):
            sum+=nums[i]
            out[i]=sum
        return out
            



        