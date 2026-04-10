class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        l = 0
        res = []
        i = 0
        while i < len(nums):
            
            
            
            if i < k :
                while q and q[-1]< nums[i]:
                    q.pop()
                q.append(nums[i])
                
            else:
                res.append(q[0])
                print(q)
                if nums[l] == q[0]:
                    q.pop(0)
                    
                l+=1
                while q and q[-1]< nums[i]:
                    q.pop()
                q.append(nums[i])
            i +=1
        # if nums[l] == q[0]:
        #     q.pop(0)
        res.append(q[0])
        return res




