class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j]==0 for j in range(cols))
        first_col_zero = any(matrix[i][0]==0 for i in range(rows))

        #mark zero - first iteration of matrix
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0 #mark the row 0
                    matrix[0][j]=0 #mark the col 0

        #post traveral - setting row and col to 0s
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        
        #handle first row and column
        if first_row_zero:
            for j in range(cols):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0]=0
        
