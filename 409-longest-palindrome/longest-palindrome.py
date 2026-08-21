class Solution:
    def longestPalindrome(self, s: str) -> int:
        map={}
        for i in s:
            if i not in map:
                map[i]=1
            else:
                map[i]+=1
        arr = list(map.values())
        count=0
        odd=False
        for j in arr:
            if j % 2 == 0:
                count+=j
            elif j%2 !=0:
                count+=j-1
                odd=True
        if odd:
            count+=1
        return count



            
        