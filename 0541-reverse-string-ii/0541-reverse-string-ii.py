class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_lst = list(s)
        length = len(s)
        for i in range(0,length,2*k):
            l=i
            r=min(i+k,length)-1
            while l<r:
                s_lst[l],s_lst[r] = s_lst[r],s_lst[l]
                l+=1
                r-=1
        return ''.join(s_lst)