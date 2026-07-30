class Solution(object):
    def findMaxLength(self, nums):
        freq = {0: -1}
        prfx_sum = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prfx_sum -= 1

            else:
                prfx_sum += 1

            if prfx_sum in freq:
                longest = max(longest, i - freq[prfx_sum])

            else:
                freq[prfx_sum] = i

        return longest



        
        