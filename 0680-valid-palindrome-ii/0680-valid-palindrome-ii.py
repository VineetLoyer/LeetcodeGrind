class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        
        def is_pal(left,right):
            l = left
            r = right
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        while left<right:
            if s[left]!=s[right]:
                return is_pal(left+1,right) or is_pal(left,right-1)
            left+=1
            right-=1
        
        return True

