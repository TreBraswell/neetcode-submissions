class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1
        second = n -1
        for i in range(m+n-1,-1,-1):
            nxt = None
            if second <=-1 or (first> -1 and nums1[first] >= nums2[second]):
                nxt = nums1[first]
                first-=1
            else:
                nxt = nums2[second]
                second -=1
            nums1[i] = nxt