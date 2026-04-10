class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        lmax = 0
        rmax= 0
        r= len(height)-1
        res = 0
        while l<=r:
            if height[l] > height[r]:
                rmax = max(rmax, height[r])
                res += rmax- height[r]
                r-=1
            else:
                lmax = max(lmax, height[l])
                res += lmax - height[l]
                l+=1
        return res