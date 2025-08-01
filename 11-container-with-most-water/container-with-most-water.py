class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_storage=0
        left=0
        right=len(height)-1
        while left<right:
            max_storage=max((right-left)*min(height[left],height[right]), max_storage)
            if height[left]<height[right]:
                left+=1
            else:    
                right-=1    
        return max_storage    




        