class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g = -1
        for i in range(len(arr)-1,-1,-1):
            t = arr[i]
            arr[i] = g
            g = max(g,t) 
        return arr