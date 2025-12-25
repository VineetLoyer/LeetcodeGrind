class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            width = right-left
            heights=min(height[left],height[right])
            cur_area = width*heights
            if cur_area>max_area:
                max_area=cur_area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
