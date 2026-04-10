class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,t = 0,0
        b,r = len(matrix),len(matrix[0])
        output = []
        while t <b and l < r:

            for i in range(l,r):
                output.append(matrix[t][i])

            print(b,t,l,r)
            t = t+1
            for i in range(t,b):
                output.append(matrix[i][r-1])
            r= r-1
            print(b,t,l,r)
            if not (l<r and t<b):
                break
            for i in range(r-1,l-1,-1):
                output.append(matrix[b-1][i])

            b = b-1
            print(b,t,l,r)
            for i in range(b-1,t-1,-1):
                output.append(matrix[i][l])
            l = l+1
            print(b,t,l,r)
        return output