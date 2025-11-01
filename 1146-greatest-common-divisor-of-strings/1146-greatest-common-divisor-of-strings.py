class Solution:
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check(s,t):
            return s==t*(len(s)//len(t))
        gcd_len = gcd(len(str1),len(str2))
        candidate = str1[:gcd_len]
        if check(str1,candidate) and check(str2,candidate):
            return candidate
        else:
            return ""