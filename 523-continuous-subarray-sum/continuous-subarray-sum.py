class Solution(object):
    def checkSubarraySum(self, nums, k):
        freq = {0:-1}
        prfx_sum = 0

        for num in range(len(nums)):
            prfx_sum += nums[num]

            need = prfx_sum % k

            if need in freq:
                if num - freq[need] >= 2:
                    return True

            else:
                freq[need] = num

        return False
            




        
        