class Solution:
    def myPow(self, x: float, n: int) -> float:
    
    # if n =0 ,return 1
    # if n is negative, use the reciprocal, and make n positive
    # multiply the result by x if the current bit is 1, then square x and halve n 
        if n==0:
            return 1
        if n<0:
            x = 1/x
            n = -n
        result = 1
        while n:
            if n%2==1:
                result*=x
            x*=x
            n//=2
        return result