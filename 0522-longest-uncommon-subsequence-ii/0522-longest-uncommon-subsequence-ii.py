class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubseq(s:str,t:str)->bool:
            i,j=0,0
            while i<len(s) and j<len(t):
                if s[i]==t[j]:
                    i+=1
                j+=1
            return i==len(s)
        
        max_len = -1
        for i in range(len(strs)):
            current_is_uncommon = True
            for j in range(len(strs)):
                if i==j:
                    continue
                if isSubseq(strs[i],strs[j]):
                    current_is_uncommon = False
                    break
            if current_is_uncommon:
                max_len = max(max_len,len(strs[i]))
        return max_len