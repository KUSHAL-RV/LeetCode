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

        if len(word1)>len(word2):
            for i in range(p1,len(word1)):
                arr.append(word1[i])
        else:
            for i in range(p2,len(word2)):
                arr.append(word2[i])
        return "".join(arr)




        