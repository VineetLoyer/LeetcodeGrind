import(
    "sort"
)
func minPairSum(nums []int) int {
        sort.Ints(nums)
        left:=0
        right:=len(nums)-1
        maxp:= 0
        for left<right{
            cur_sum:= nums[left]+nums[right]
            if cur_sum>=maxp{
                maxp=cur_sum
            }
            left+=1
            right-=1
        }
        return maxp
}