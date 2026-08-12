class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr=set()
        n=len(nums)
        sum=0
        target=0
        for k in range(n):
            sum+=nums[k]
        if sum % 2 != 0:
            return False

        target=sum//2
            
        arr.add(nums[n-1])
        for i in range(n-2,-1,-1):
            current=nums[i]
            new_sums = set()
            for j in arr:
                new_sums.add(j+current)
            arr.update(new_sums)
        if target in arr:
            return True
        else:
            return False

        