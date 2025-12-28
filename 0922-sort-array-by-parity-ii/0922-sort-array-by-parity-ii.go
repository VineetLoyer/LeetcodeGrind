func sortArrayByParityII(nums []int) []int {
        n:= len(nums)
        even_ptr:= 0
        odd_ptr:= 1
        for even_ptr<n && odd_ptr<n{
            for even_ptr<n && nums[even_ptr]%2==0{
                even_ptr+=2
            }
            for odd_ptr<n && nums[odd_ptr]%2!=0{
                odd_ptr+=2
            }
            if even_ptr<n && odd_ptr<n{
                nums[even_ptr],nums[odd_ptr]=nums[odd_ptr],nums[even_ptr]
                even_ptr+=2
                odd_ptr+=2
            }
        }
        return nums
}