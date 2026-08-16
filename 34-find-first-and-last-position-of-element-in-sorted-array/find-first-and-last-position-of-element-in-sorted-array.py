class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if low < len(nums) and nums[low] == target:
            first = low

            low = 0
            high = len(nums)-1 

            while low <= high:           
                mid = (low + high) // 2

                if nums[mid] <= target:
                    low = mid + 1

                else:
                    high = mid - 1

            return [first, high]
        
        return [-1, -1]  
    
            