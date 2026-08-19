class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        low = 1
        high = max(position) - min(position)

        while low <= high:
            mid = (low + high) // 2

            ball = 1
            last = position[0]

            for pos in position:
                if pos - last >= mid:
                    ball += 1
                    last = pos

            if ball >= m:
                low = mid + 1
            
            else:
                high = mid - 1

        return high
