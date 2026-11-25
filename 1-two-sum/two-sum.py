class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(nums)):
            summ=target-nums[i]
            if summ in seen:
                return [seen[summ],i]
            seen[nums[i]]=i
