class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(arr)-1
        while l<r:
            m = (l+r)//2
            if l == m or r==m:
                break
            if arr[m]> x:
                r= m
            elif arr[m] <x:
                l = m
            else:
                l = m
                break
        if abs(arr[l] - x) > abs(arr[r] -x):
            l = r
        r = l
        while r-l<k-1:
            if r == len(arr)-1:
                l-=1
            elif l == 0:
                r+=1
            elif abs(arr[l-1] - x) <= abs(arr[r+1]-x):
                l-=1
            else:
                r+=1
        return arr[l:r+1]


