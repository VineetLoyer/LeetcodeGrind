func shortestDistance(wordsDict []string, word1 string, word2 string) int {
        min_dis:= 50000
        index1 := -1
        index2 := -1
        for i:=0; i<len(wordsDict);i++{
            if wordsDict[i]==word1{
                index1 = i
            }
            if wordsDict[i]==word2{
                index2 = i
            }
            if index1!=-1 && index2!=-1{
                min_dis = min(min_dis,abs(index2-index1))
            }
        }
        return min_dis
}
func abs(x int) int{
    if x<0 {return -x}
    return x
}