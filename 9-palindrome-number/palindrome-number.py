class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        p=0
        q=len(s)-1
        while p<q:
            if s[p]==s[q]:
                p+=1
                q-=1
            else:
                return False
        return True
        