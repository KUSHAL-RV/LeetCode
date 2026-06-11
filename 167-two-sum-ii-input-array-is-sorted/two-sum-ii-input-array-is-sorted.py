class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        start=0
        end=len(numbers)-1
        res=[]
        

        
        while start<end:
            s=numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]
            elif s<target:
                start+=1
            else:
                end-=1
        
            


        