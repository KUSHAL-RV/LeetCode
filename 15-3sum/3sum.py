class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        a=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            p1=i+1
            p2=n-1
            while p1<p2:
                sum=nums[i]+nums[p1]+nums[p2]
                if sum>0:
                    p2-=1
                elif sum<0:
                    p1+=1
                else:
                    a.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                    while p1<p2 and nums[p1]==nums[p1-1]:
                        p1+=1
                    while p1<p2 and nums[p2]==nums[p2+1]:
                        p2-=1
        return a        