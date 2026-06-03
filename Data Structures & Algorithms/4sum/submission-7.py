class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        nums.sort()
        print(nums)
        def k_sum(k,ii,s):
            if k!=2:
                for i in range(ii,len(nums)):
                    if i>0 and nums[i] == nums[i-1] and i != ii:
                        continue
                    curr.append(nums[i])
                    
                    k_sum(k-1,i+1,s+nums[i]) 
                    curr.pop()
            else:
                l = ii
                r = len(nums)-1
                while l <r:
                    result = nums[r] + nums[l] + s
                    if result> target:
                        r-=1
                    elif result<target:
                        l+=1
                    else:
                        res.append(curr+[nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
        k_sum(4,0,0)
        return res