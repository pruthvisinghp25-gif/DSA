class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (high + low) // 2

            parts = 1
            count = 0
            
            for num in nums:
                if count + num > mid:
                    parts += 1
                    count = 0

                count += num

            if parts <= k:
                high = mid - 1

            else:
                low = mid + 1

        return low