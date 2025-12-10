class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        def ispal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        while left < right:
            if s[left]!=s[right]:
                return ispal(left+1,right) or ispal(left,right-1)
            
            left+=1
            right-=1
        return True