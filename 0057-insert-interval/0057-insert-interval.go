func insert(intervals [][]int, newInterval []int) [][]int {
        n:= len(intervals)
        i:= 0
        res := [][]int{}
        for i<n && intervals[i][1]<newInterval[0]{
            res=append(res,intervals[i])
            i+=1
        }
        for i<n && intervals[i][0]<=newInterval[1]{
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        }
        res=append(res,newInterval)

        for i<n{
            res=append(res,intervals[i])
            i+=1
        }
        return res
}