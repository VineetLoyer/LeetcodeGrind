class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        while left<right:
            if ('a'<=s[left]<='z' or 'A'<=s[left]<='Z' or '0'<=s[left]<='9'):
                if ('a'<=s[right]<='z' or 'A'<=s[right]<='Z' or '0'<=s[right]<='9'):
                    if s[left]==s[right]:
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left+=1
        return True