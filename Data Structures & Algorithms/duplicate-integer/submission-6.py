class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set()
        for i in nums:
            if i in k :
                return True
            k.add(i)
        return False