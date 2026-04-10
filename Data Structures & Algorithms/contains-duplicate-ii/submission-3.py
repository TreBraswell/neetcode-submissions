class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        if k ==0:
            return False
        l = 0
        for i in range(len(nums)):
            if i <k+1:
                if nums[i] in s:
                    return True
                s.add(nums[i])
            else:
                s.remove(nums[l])
                if nums[i] in s:
                    return True
                s.add(nums[i])
                l+=1
        return False