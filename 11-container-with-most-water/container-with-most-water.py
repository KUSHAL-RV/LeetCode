class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0;
        end=len(height)-1
        max=0
      

        while start<end:
            h=min(height[start],height[end]) 
            w=end-start
            a=h*w
            if a>max:
                max=a
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return max

        
            

            
            
            