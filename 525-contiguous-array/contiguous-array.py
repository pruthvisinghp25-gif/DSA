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

            if need in freq:
                length = i - freq[need]

                if length > count:
                    count = length

            if need not in freq:
                freq[need] = i

        return count 