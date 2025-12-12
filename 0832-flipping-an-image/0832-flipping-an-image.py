class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #phase 1: swapping elements in rows
        for row in image:
            left =  0
            right = len(row)-1
            while left<right:
                row[left],row[right]=row[right],row[left]
                left+=1
                right-=1
        
        #phase 2: inverting: converting 0s to 1s and vice versa
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col]==0: 
                    image[row][col]=1
                else:
                    image[row][col]=0
        return image
