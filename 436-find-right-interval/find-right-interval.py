class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        arr_s=[]
        arr_e=[]
        for i in range(n):
            arr_s.append([intervals[i][0],i])
            arr_e.append(intervals[i][1])
        res=[]
        arr_s.sort(key=lambda x: x[0])
        for j in arr_e:
            best=-1
            left=0
            right=n-1
            while left<=right:
                mid=(left+right)//2
                if arr_s[mid][0]>=j:
                    best=arr_s[mid][1]
                    right=mid-1
                else:
                    left=mid+1
            res.append(best)
        
        return res






        