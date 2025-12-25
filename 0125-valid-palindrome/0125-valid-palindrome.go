import("unicode")

func isPalindrome(s string) bool {
    left:=0
    right:=len(s)-1
    for left<right{
        lChar:= rune(s[left])
        if !isAlphaNumeric(lChar){
            left++
            continue
        }
        rChar:=rune(s[right])
        if !isAlphaNumeric(rChar){
            right--
            continue
        }
        if unicode.ToLower(lChar)!=unicode.ToLower(rChar){
            return false
        }
        left++
        right--
    }
    return true
}

func isAlphaNumeric(r rune) bool{
    return unicode.IsNumber(r)||unicode.IsLetter(r)
}