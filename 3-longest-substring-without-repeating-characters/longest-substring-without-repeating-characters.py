class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=set()
        l=0
        max_len=0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            size=r-l+1
            if size>max_len:
                max_len=size
            
        return max_len

        