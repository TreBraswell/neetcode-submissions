class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix[0])
        c = r
        while l <r :
            c = int(math.ceil(c/2))
            print(c)
            for i in range(r-l-1):
                tl = matrix[l][l+i]
                tr = matrix[l+i][r-1]
                br = matrix[r-1][r-1-i]
                bl = matrix[r-1-i][l]
                matrix[l][l+i] = bl
                matrix[l+i][r-1] = tl
                matrix[r-1][r-1-i] = tr
                matrix[r-1-i][l] = br
            
            l +=1
            r -=1
        