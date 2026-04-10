class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r= len(arr)-1
        while l<r:
            
            m = (l +r)//2
            if m == r or l == m:
                break
            
            if arr[m]> x:
                r = m
            elif arr[m]< x:
                l = m
            else:
                l = m
                break
        if x-arr[l] > arr[r]-x:
            l=r
        r = l
        while r -l < len(arr)-1 and r- l< k-1:
            print(abs(x-arr[l]), abs(arr[r]-x))
            if l == 0:
                r +=1
            elif r == len(arr)-1:
                l-=1
            elif x-arr[l-1] > arr[r+1]-x:
                r+=1
            else:
                l -=1

        return arr[l:r+1]