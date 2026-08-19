class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)

        if m * k > len(bloomDay):
            return -1

        while low <= high:
            mid = (high + low) // 2

            flowers = 0
            bou = 0
            
            for bloom in bloomDay:
                
                if bloom <= mid:
                    flowers += 1

                    if flowers == k:
                        bou += 1
                        flowers = 0

                else:
                    flowers = 0

            if bou >= m:
                high = mid - 1

            else:
                low = mid + 1

        return low