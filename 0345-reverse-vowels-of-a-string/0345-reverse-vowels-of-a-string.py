class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('A','a','E','e','I','i','O','o','U','u')
        left = 0
        right = len(s)-1
        s_lst = list(s)
        while left<right:
            while left<right and s_lst[left] not in vowels:
                left+=1
            while left<right and s_lst[right] not in vowels:
                right-=1
            
            s_lst[left],s_lst[right]=s_lst[right],s_lst[left]
            left+=1
            right-=1
        return ''.join(s_lst)
