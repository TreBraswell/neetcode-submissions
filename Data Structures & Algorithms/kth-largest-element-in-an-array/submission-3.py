class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            res.append(nums[i]*-1)
        heapq.heapify(res)
        for i in range(k-1):
            heapq.heappop(res)
        return heapq.heappop(res) *-1