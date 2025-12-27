func compress(chars []byte) int {
        write:= 0
        read:= 0
        for read < len(chars){
            char:= chars[read]
            count:= 0

            for read < len(chars) && chars[read]==char{
                read+=1
                count+=1
            }
            
            chars[write]=char
            write+=1

            if count>1{
                s:=strconv.Itoa(count)
                for k:=0;k<len(s);k++{
                    chars[write] = s[k]
                    write+=1
                }
            }
        }
        return write
}