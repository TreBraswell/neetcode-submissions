class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        if len(a) > len(b):
            a,b = b,a
        full = len(a) + len(b)
        half = full//2
        l = 0
        r = len(a)-1
        while True:
            i = (l +r)//2
            j = half - i - 2
            a_l = a[i] if i >=0 else float('-inf')
            a_r = a[i +1] if i +1 < len(a) else float('inf')
            b_l = b[j] if j >= 0 else float('-inf')
            b_r = b[j +1] if j +1 < len(b) else float('inf')
            print(a_l,a_r,b_l,b_r, i,j)
            if b_r>= a_l:
                if full % 2 == 0:
                    return (max(a_l,b_l) + min(a_r,b_r))/2
                else:
                    return min(a_r,b_r)
            elif a_r > b_l:
                r = i -1
            else:
                l = i +1
