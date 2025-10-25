class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = n*n
        
        # Expected Sum and Sum of Squares
        #sum = 1 + 2 + ... + n = n(n+1)//2
        sum1 = m*(m+1)//2
        sumsq1 = m*(m+1)*(2*m + 1)//6 
        
        # Actual Sum and Sum of Squares
        sumA = 0
        sumsqA = 0
        for row in grid:
            for v in row:
                sumA += v
                sumsqA += v*v
        
        # from maths, say missing = a, repeated = b => a-b = sumA - sum
        d1 = sum1 - sumA
        # print(f"d1 = {d1}")
        # from maths, sumsq - sumsqA = (a-b)(a+b)
        d2 = sumsq1 - sumsqA
        # print(f"d2 = {d2}")
        
        #I can say, d2 = (d1)(a+b); so, a+b =  d2/d1
        div = d2//d1
        # print(f"div ={div}")
        # from math, a = div - b and a-b = d1 => a = (div+d1)//2
        a = (div + d1)//2 
        # print(f"a = {a}")
        b = div - a
        # print(f"b = {b}")
        return [b,a]