class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        LIS=[1]*n
        LIS[n-1]=1
        for i in range(n-2,-1,-1):
            current=nums[i]
            for j in range(n-1,i,-1):
                if nums[j]>current:
                    LIS[i]=max(LIS[i], 1 + LIS[j])
        return max(LIS)





