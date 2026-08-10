from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for num in range(len(nums)):
            while dq and nums[num] > nums[dq[-1]]:
                dq.pop()

            dq.append(num)

            if dq[0] <= num - k:
                dq.popleft()
                
            if num >= k - 1:
                ans.append(nums[dq[0]])

        return ans

        