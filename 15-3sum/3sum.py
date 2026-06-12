class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import numpy as np
        nums=np.sort(nums)
        
        res=[]
        
        
        for i ,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            start=i
 
            p1=start+1
            p2=len(nums)-1
            out=[]
            while p1<p2:
                s=a+nums[p1]+nums[p2]
                if s<0:
                    p1+=1
                        
                elif s>0:
                    p2-=1
                else :
                    res.append([a,nums[p1],nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
            
        return res

        

        



        