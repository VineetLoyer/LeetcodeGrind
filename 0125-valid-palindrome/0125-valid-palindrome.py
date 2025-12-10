class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower()==s[right].lower():
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left+=1
        return True