class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        turb = ""
        l = 0

        res = 1 
        for r in range(1,len(arr)):
            print(l,r,res,turb, arr[r-1], arr[r])
            if arr[r-1] > arr[r] and turb !='>':
                res = max(res, r-l+1)
                turb = '>'
            elif arr[r-1] < arr[r] and turb !='<':
                res = max(res, r-l+1)
                turb = '<'
            else:
                if arr[r-1] == arr[r]:
                    l = r
                else:
                    l =r-1
                
        return res
                    