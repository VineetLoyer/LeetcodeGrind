class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        squares = n*m

        # limits of spiral-matrix
        top_limit = 0
        bottom_limit = n-1
        left_limit = 0
        right_limit = m-1

        # moving 
        x,y=0,0 # col x , row y
        x_inc = 1
        y_inc = 0
        # (1,0) = moving right
        # (0,1) = moving down
        # (-1,0) = moving left
        # (0,-1) = moving up

        results= []
        while len(results)<squares:
            results.append(matrix[y][x])
            if x_inc==1 and y==top_limit and x==right_limit: # if we reached the top-right corner
                y_inc = 1
                x_inc = 0 
                top_limit+=1 
            
            if y_inc==1 and y==bottom_limit and x==right_limit:# if we reached bottom-right corner
                y_inc = 0
                x_inc = -1
                right_limit-=1
            
            if x_inc==-1 and y==bottom_limit and x==left_limit: #if we reached bottom-left corner - move up and decrease the bottom up limit
                y_inc = -1
                x_inc = 0
                bottom_limit-=1
            if y_inc == -1 and y==top_limit and x==left_limit:# if we reached top-left corner - move right and decrese the left wall
                y_inc = 0
                x_inc = 1
                left_limit+=1
            x+=x_inc
            y+=y_inc
        return results





