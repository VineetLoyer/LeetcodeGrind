class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix) #number of rows
        cols = len(matrix[0]) #cols = numbner of elements in first row

        first_row_zeros = any(matrix[0][c]==0 for c in range(cols)) # True if first row has 0
        first_col_zeros = any(matrix[r][0]==0 for r in range(rows)) # True if first col has 0

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0 # mark the corresponding first row and first col element as 0
                    matrix[r][0]=0

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
 
        if first_row_zeros:
            for c in range(cols):
                matrix[0][c]=0
        if first_col_zeros:
            for r in range(rows):
                matrix[r][0]=0




        