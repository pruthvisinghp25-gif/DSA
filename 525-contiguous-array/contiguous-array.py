class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        freq = {0 : -1}
        count = 0
        prfx_sum = 0

        for i, num in enumerate(nums):
            if num == 0:
                prfx_sum -= 1

            else:
                prfx_sum += 1

            need = prfx_sum 

            if prfx_sum in freq:
                length = i - freq[prfx_sum]

                if length > count:
                    count = length

            if prfx_sum not in freq:
                freq[prfx_sum] = i

        return count 