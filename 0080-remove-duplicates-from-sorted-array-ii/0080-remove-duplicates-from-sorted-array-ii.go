func removeDuplicates(nums []int) int {
        n:= len(nums)
        if n<=2{
            return n
        }
        index:= 2
        for fast:=2; fast<n; fast++{
            if nums[fast]!=nums[index-2]{
                nums[index] = nums[fast]
                index+=1
            }
        }
        return index
}