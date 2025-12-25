func trap(height []int) int {
        n:= len(height)
        if n==0{
            return 0
        }
        max_left:= make([]int, n)
	    max_right:= make([]int, n)
        current_max:= 0
        for i:=0; i<n;i++{
            current_max = max(current_max,height[i])
            max_left[i]=current_max
        }
        current_max = 0
        for i:=n-1; i>=0;i--{
            current_max = max(current_max,height[i])
            max_right[i]=current_max
        }
        total_water:= 0
        for i:=0;i<n;i++{
            water_at_i:= min(max_left[i],max_right[i]) - height[i]
            total_water+=water_at_i
        }
        return total_water
}