class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest = len(nums)
        s1 = 0
        s2 = 0
        for item in range(largest + 1):
            s1 ^= item
        for num in nums:
            s2 ^= num
        return s1 ^ s2
"""You should know how the bitwise operators work before using this method. 
Bitwise method is quite efficient in some cases, for example, you can use 
a & 1 == 0 instead of a//2 == 0 while you want to know if a is an even number or not.
"""