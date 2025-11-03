class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            rows = [1]*(i+1) #append all ones
            for j in range(1,i):
                rows[j]=triangle[i-1][j] + triangle[i-1][j-1]
            triangle.append(rows)
        return triangle