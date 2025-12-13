class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        
        #1. fill max_left
        current_max = 0
        for i in range(n):
            current_max = max(current_max,height[i])
            max_left[i] = current_max
        
        #2. fill max_right
        current_max = 0
        for i in range(n-1,-1,-1):
            current_max = max(current_max,height[i])
            max_right[i] = current_max
        
        #3. calculate collected water
        total_water = 0
        for i in range(n):
            water_at_i = min(max_left[i],max_right[i]) - height[i]
            total_water+=water_at_i
        return total_water