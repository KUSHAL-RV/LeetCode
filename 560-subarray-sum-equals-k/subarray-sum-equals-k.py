class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap={0:1}
        p_sum=0
        c=0
        for i in range(len(nums)):
            p_sum+=nums[i]
            rem=p_sum-k
            if rem in hmap:
                c+=hmap[rem]
            hmap[p_sum]=hmap.get(p_sum,0)+1
        return c
