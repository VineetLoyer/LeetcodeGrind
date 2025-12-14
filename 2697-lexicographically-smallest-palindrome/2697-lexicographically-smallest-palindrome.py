class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_lst = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]==s[right]:
                #if same, move on
                left+=1
                right-=1
            else:
                #else, replace with min lexcigraphic char
                minc = min(s[left],s[right])
                s_lst[left],s_lst[right]=minc,minc
                left+=1
                right-=1
        return ''.join(s_lst)