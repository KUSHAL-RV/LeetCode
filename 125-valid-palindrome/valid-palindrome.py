class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str1=''.join(char for char in s if char.isalnum())
        n=len(str1)
        arr=list(str1)
        s=0
        l=n-1
        while l>s:
            if arr[s]!=arr[l]:
                return False
            else:
                s+=1
                l-=1
        return True

        