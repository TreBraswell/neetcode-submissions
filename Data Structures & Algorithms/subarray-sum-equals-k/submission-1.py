class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        s = defaultdict(int)
        s[0] =1
        res = 0
        for i in nums:
            cur_sum += i
            d = cur_sum - k
            res += s[d]
            s[cur_sum] +=1
        return res 