func sortedSquares(nums []int) []int {
    n:=len(nums)
    res:=make([]int,n)
    left:=0
    right:=n-1
    for i:=n-1;i>=0;i-- {
        lsq:=nums[left]*nums[left]
        rsq:=nums[right]*nums[right]
        if lsq>rsq{
            res[i]=lsq
            left++
        }else{
            res[i]=rsq
            right--
        }
    }
    return res
}