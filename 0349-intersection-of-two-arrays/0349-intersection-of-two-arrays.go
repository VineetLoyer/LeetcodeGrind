func intersection(nums1 []int, nums2 []int) []int {
    a:= append([]int(nil),nums1...) 
    b:= append([]int(nil),nums2...)
    sort.Ints(a)
    sort.Ints(b)

    i,j:=0,0

    res:=make([]int,0)

    for i<len(a) && j<len(b){
        if a[i]<b[j]{
            i++
        }else if b[j]<a[i]{
            j++
        }else{
            if len(res)==0 || res[len(res)-1]!=a[i]{
                res = append(res,a[i])
            }
            i++
            j++
        }
    }
    return res
}