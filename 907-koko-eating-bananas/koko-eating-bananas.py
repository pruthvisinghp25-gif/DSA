class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (high + low) // 2
            hours = 0
            
            for pile in piles:
                hours += (mid + pile - 1) // mid

            if hours <= h:
                high = mid - 1

            else:
                low = mid + 1

        return low 
