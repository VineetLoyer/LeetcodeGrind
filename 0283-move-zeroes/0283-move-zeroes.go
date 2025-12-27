func moveZeroes(nums []int)  {
    index:=0
    for fast:=0;fast<len(nums);fast++{
        if nums[fast]!=0{
            nums[fast],nums[index]=nums[index],nums[fast]
            index++
        }
    }
}