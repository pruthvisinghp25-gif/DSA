class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        rem = total % p
        
        if rem == 0:
            return 0

        freq = {0 :-1}
        prfx_sum = 0
        lent = len(nums)

        for i in range(len(nums)):
            prfx_sum += nums[i]
            
            curr = prfx_sum % p 
            need = (curr - rem) % p

            if need in freq:
                lent = min(lent, i - freq[need])

            freq[curr] = i

        return lent if lent != len(nums) else -1
    



        

        