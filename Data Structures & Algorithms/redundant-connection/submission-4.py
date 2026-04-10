class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(i):
            if i != par[i]:
                par[i] = find(par[i])
            return par[i]
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
               rank[p1] +=1 
               par[p2] = par[p1]
            else:
                rank[p2] +=1
                par[p1] = par[p2]
            return True
        for x,y in edges:
            if not union(x,y):
                return [x,y]

                


        