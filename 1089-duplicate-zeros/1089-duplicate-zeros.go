func duplicateZeros(arr []int)  {
        zeros:= 0
        for num:=0;num<len(arr);num++{            
            if arr[num]==0{
                zeros+=1
            }
        }
        n:= len(arr)
        for i:=n-1;i>-1;i--{
            if i+zeros < n{
                arr[i+zeros] = arr[i]
            }
            if arr[i]==0{
                zeros-=1
                if i+zeros<n{
                    arr[i+zeros]=0
                }
            }
        }
}