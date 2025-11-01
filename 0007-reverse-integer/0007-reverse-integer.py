class Solution:
    def reverse(self, x: int) -> int:
        rev_number = 0
        sign = -1
        if x<0:
            x*=sign
        else:
            sign = 1
        
        while x>0:
            last_digit = x % 10
            if rev_number > 214748364 or (rev_number == 214748364 and last_digit > 7):
                return 0
            if rev_number < -214748364 or (rev_number == -214748364 and last_digit < -8):
                return 0
            rev_number = rev_number * 10 + last_digit
            x = x // 10
        
        if sign !=1:
            rev_number*=-1
        
        return rev_number
