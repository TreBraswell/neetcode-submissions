class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) -1
        res = 0
        maxl = 0
        maxr = 0
        while l<r :
            if height[l]>height[r]:
                res += max(maxr - height[r],0)
                maxr = max(maxr,height[r])
                r -= 1
            else:
                res += max(maxl-height[l],0)
                maxl = max(maxl,height[l])
                l+=1
        return res