class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L,M,R):
            left = nums[L:M+1]
            right = nums[M+1:R+1]
            l1,l2,i = 0,0,L
            while l2<len(right) and l1 < len(left):
                if right[l2] > left[l1]:
                    nums[i] = left[l1]
                    l1 +=1
                else:
                    nums[i] = right[l2]
                    l2 +=1
                i +=1
            while l2<len(right):
                nums[i] = right[l2]
                l2 +=1
                i +=1
            while l1<len(left):
                nums[i] = left[l1]
                l1 +=1
                i +=1
        
        def split(l,r):
            if l>=r:
                return 
            m = (l+r)//2
            split(l,m)
            split(m+1,r)
            merge(l,m,r)
        split(0,len(nums)-1)
        return nums