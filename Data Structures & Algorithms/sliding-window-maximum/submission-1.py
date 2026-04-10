import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = []
        result = []
        largest = -1001
        for i in range(k):
            largest = max(largest,nums[i])
            window.append(nums[i])
        result.append(largest)
        for r in range(k,len(nums)):
            window.pop(0)
            window.append(nums[r])
            if nums[l] == largest and nums[l]>nums[r]:
                largest = max(window)
            else:
                
                largest = max(largest,nums[r])
            l = l +1
            result.append(largest)
        return result

            