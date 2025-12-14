class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_lst = list(s)
        left = 0
        right = len(s)-1

        while left<right:
            if 'a'<=s[left]<='z' or 'A'<=s[left]<='Z':
                if 'a'<=s[right]<='z' or 'A'<=s[right]<='Z':
                    s_lst[left],s_lst[right]=s_lst[right],s_lst[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return ''.join(s_lst)