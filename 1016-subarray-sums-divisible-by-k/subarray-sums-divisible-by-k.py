class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        freq = {0 : 1}
        count = 0
        prfx_sum = 0

        for num in nums:
            prfx_sum += num

            need = prfx_sum % k

            if need in freq:
                count += freq[need]

            freq[need] = freq.get(need, 0)+1

        return count 
                

