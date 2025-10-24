class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        #placeholders for first row and first col
        first_row_zero = any(matrix[0][j]==0 for j in range(cols))
        first_col_zero = any(matrix[i][0]==0 for i in range(rows))

        #step2:traverse the matrix and set first row/col elements to 0 (first row and first col are placeholders)
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        #step3: traverse the matrix and update the elements to 0, based on placeholders.
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        #lastly, make the first row/col to 0, based on flag.
        if first_row_zero:
            for j in range(cols):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0]=0
