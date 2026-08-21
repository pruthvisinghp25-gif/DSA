class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = max(candies)

        while low <= high:
            mid = (high + low) // 2

            count= 0
            
            for cndy in candies:
                count += cndy // mid

            if count >= k:
                low = mid + 1

            else:
                high = mid - 1

        return high


        