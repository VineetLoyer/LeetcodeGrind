func isSubsequence(s string, t string) bool {
        i,j:=0,0
        if len(s)>len(t){
            return false
        }
        if len(s)==0{
            return true
        }
        for i<len(s) && j<len(t){
            if s[i]==t[j]{
                i+=1
            }
            j+=1
        }
        return i == len(s)
}