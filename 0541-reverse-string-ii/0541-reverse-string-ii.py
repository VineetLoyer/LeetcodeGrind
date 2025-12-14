class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_lst = list(s)
        for i in range(0,len(s),2*k):
            s_lst[i:i+k]=reversed(s_lst[i:i+k])
        return "".join(s_lst)
