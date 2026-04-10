class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,m,r):
            left = nums[l:m+1]
            right = nums[m+1:r+1]
            l1 = 0
            i = l
            l2 =0
            while l1<=len(left)-1 and l2<=len(right)-1:
                
                if left[l1]<right[l2]:
                    nums[i] = left[l1]
                    l1 +=1
                else:
                    nums[i] = right[l2]
                    l2 +=1
                i+=1
            while l1<=len(left)-1:
                nums[i] = left[l1]
                l1 +=1
                i+=1
            while l2<=len(right)-1:
                nums[i] = right[l2]
                l2 +=1
                i+=1
        def split(l,r):
            
            if l ==r:
                return 
            
            m = (l+r)//2
            split(l,m)
            split(m+1,r)
            merge(l,m,r)

        split(0,len(nums)-1)
        return nums
