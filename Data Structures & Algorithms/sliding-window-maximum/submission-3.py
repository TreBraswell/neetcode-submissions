import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # too slow
        # l = 0
        # window = []
        # result = []
        # largest = -1001
        # for i in range(k):
        #     largest = max(largest,nums[i])
        #     window.append(nums[i])
        # result.append(largest)
        # for r in range(k,len(nums)):
        #     window.pop(0)
        #     window.append(nums[r])
        #     if nums[l] == largest and nums[l]>nums[r]:
        #         largest = max(window)
        #     else:
                
        #         largest = max(largest,nums[r])
        #     l = l +1
        #     result.append(largest)
        # return result
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            print('this is l and r :',l, ' : ',r)
            while q and nums[q[-1]] < nums[r]:
                print("this is q while popping loop : ",q)
                q.pop()
            q.append(r)

            if l > q[0]:
                print('popped left')
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
            print('this is q after loop : ',q)
        return output

            