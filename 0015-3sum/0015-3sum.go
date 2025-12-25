import(
    "sort"
)
func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    var res[][] int
    for i:=0; i<len(nums)-2;i++{
        if i>0 && nums[i]==nums[i-1]{
            continue
        }
        left:=i+1
        right:=len(nums)-1
        for left<right{
            sum_cur:=nums[i]+nums[left]+nums[right]
            if sum_cur<0{
                left++
            }else if sum_cur>0{
                right--
            }else{
                res = append(res, []int{nums[i], nums[left], nums[right]})
                for left<right && nums[left]==nums[left+1]{
                    left++
                }
                for left<right && nums[right]==nums[right-1]{
                    right--
                }
                left++
                right--
            }
        }
    }
    return res
    
}