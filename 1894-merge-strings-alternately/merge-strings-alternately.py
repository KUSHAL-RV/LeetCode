class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr=[]
        p1=0
        p2=0
        l1=min(len(word1),len(word2))
        

        for i in range(l1):
            arr.append(word1[p1])
            p1+=1
            arr.append(word2[p2])
            p2+=1

        arr.append(word1[p1:])
        arr.append(word2[p2:])
        return "".join(arr) 





        