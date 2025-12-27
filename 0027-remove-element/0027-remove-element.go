func removeElement(nums []int, val int) int {
    index:=0
    for fast:=0;fast<len(nums);fast++{
        if nums[fast]!=val{
            nums[index]=nums[fast]
            index+=1
        }
    }
    return index
}