class Solution(object):
    def maxArea(self,height):
        max_area=0
        left=0
        right=len(height)-1
        while left<right:
            breadth=right-left
            length=min(height[left],height[right])
            area=breadth*length
            max_area=max(max_area,area)
            
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
                
        return max_area
