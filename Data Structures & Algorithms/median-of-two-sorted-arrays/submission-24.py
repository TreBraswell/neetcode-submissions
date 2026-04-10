class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        middle_partion = (len(nums1) + len(nums2))//2
        l = 0 
        r = len(nums1)-1
        while True:
            i = (l+r)//2
            j = middle_partion - i - 2
            l1 = nums1[i] if i >=0 else float("-inf")
            r1 = nums1[i+1] if i +1< len(nums1) else float("inf")
            l2 = nums2[j] if j>= 0 else float("-inf")
            r2 = nums2[j+1] if j+1 <len(nums2) else float("inf")
            if l1 <= r2 and r1>= l2:
                if (len(nums1) + len(nums2))%2:
                    return min(r1,r2)
                return (max(l1,l2) + min(r1,r2))/2
            elif r1<l2:
                l = l +1
            else:
                r = r -1 