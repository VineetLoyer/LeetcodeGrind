func findMaxConsecutiveOnes(nums []int) int {
        maxsofar:=0
        count:=0
        for num:=0;num<len(nums);num++{
            if nums[num]==1{
                count+=1
                maxsofar=max(maxsofar,count)
            }else{
                count = 0
            }
        }
        return maxsofar
}