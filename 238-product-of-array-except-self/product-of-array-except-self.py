class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[1]*n
        pre=1
        suf=1

        for i in range(n):
            j=n-1-i
            ans[i]=ans[i]*pre
            pre*=nums[i]

            ans[j]=ans[j]*suf
            suf*=nums[j]
        return ans            
            

        