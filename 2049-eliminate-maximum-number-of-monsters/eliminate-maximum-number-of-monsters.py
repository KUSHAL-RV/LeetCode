class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count=0
        at=[]
        for c in range(0,len(dist)):
            at.append(dist[c]/speed[c])
        at.sort()
        for c1 in range(0,len(at)):
            if at[c1]>c1:
                count+=1

            else:
                break
        return count 
