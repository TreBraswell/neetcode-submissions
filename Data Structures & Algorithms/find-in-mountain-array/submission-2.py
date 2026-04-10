class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        leng = mountainArr.length()
        l = 0
        r = leng-1
        middle= 0
        while l <=r: 
            print('calculating middle', l,r)
            m = (l+r)//2
            if mountainArr.get(m-1)<mountainArr.get(m)<mountainArr.get(m+1):
                l = m+1
            elif mountainArr.get(m-1)>mountainArr.get(m)>mountainArr.get(m+1):
                r = m -1
            else:
                middle = m
                break
        
        l = 0
        r = middle
        print(middle)
        while l<=r:
            print(l,r)
            m= (l+r)//2

            if mountainArr.get(m) > target:
                r = m-1
            elif mountainArr.get(m)<target:
                l = m +1
            else:
                return m

        l = middle
        r = leng-1
        while l<=r:
            m= (l+r)//2
            if mountainArr.get(m) > target:
                l = m +1
            elif mountainArr.get(m)<target:
                r = m -1
            else:
                return m
        return -1