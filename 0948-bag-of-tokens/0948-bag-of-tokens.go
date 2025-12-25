import(
    "sort"
)
func bagOfTokensScore(tokens []int, power int) int {
        sort.Ints(tokens)
        left:= 0
        right:= len(tokens)-1
        score:= 0
        max_score:= 0
        for left<=right{
            if tokens[left]<=power{
                power-=tokens[left]
                score+=1
                left+=1
                max_score=max(max_score,score)
            }else if score>0{
                power+=tokens[right]
                score-=1
                right-=1
            }else{
                break
            }
        }
        return max_score
}