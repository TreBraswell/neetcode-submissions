class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nm1 = nums1
        nm2 = nums2
        if len(nums2)<len(nums1):
            nm1 = nums2
            nm2 = nums1
        l1 = len(nm1)
        l2 = len(nm2)
        t = l1 + l2
        half = t//2
        l = 0
        r = l1 - 1
        while True:
            i = (l+r)//2 # A
            j = half - i -2 # B
            nm1_l = nm1[i] if i >=0 else float("-inf") # small left
            nm1_r = nm1[i+1] if (i+1) < len(nm1) else float("inf") # small right
            nm2_l = nm2[j] if j>= 0 else float("-inf") # big left
            nm2_r = nm2[j+1] if (j+1) <len(nm2) else float("inf") 
            if nm1_l<= nm2_r and nm2_l <= nm1_r:
                print(t,' ',t%2, ' ', nm1_r,' ',nm2_r)
                if t%2==1:
                    print('odd case')
                    return min(nm1_r,nm2_r)
                return (max(nm1_l,nm2_l)+ min(nm1_r,nm2_r))/2
            elif nm1_l>nm2_r:
                r = i - 1
            else:
                l = i +1