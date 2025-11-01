class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if the number is negative, it cannot be a pallindrome
        # if number contains 0 at end and is not 0 it is not a pallindrome
        if x<0 or (x%10==0 and x!=0):
            return False
        if x==0:
            return True
        rev_num=0
        original = x
        while x>0:
            last_dig=x%10
            rev_num = rev_num*10+last_dig
            x//=10
        return original==rev_num
