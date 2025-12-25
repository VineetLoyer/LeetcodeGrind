import(
    "sort"
)
func numRescueBoats(people []int, limit int) int {
        sort.Ints(people)
        left:= 0
        right:= len(people)-1
        boat:= 0
        for left<=right{
            if people[left]+people[right]<=limit{
                boat+=1
                left+=1
                right-=1
            }else{
                boat+=1
                right-=1
            }
        }
        return boat
}