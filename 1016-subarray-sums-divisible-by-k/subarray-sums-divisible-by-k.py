class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        freq = {0 : 1}
        count = 0
        prfx_sum = 0

        for num in nums:
            prfx_sum += num

            rem = prfx_sum % k

            if rem in freq:
                count += freq[rem]

            if rem not in freq:
                freq[rem] = 1

            else:
                freq[rem] += 1
            # freq[rem] = freq.get(rem, 0)+1

        return count 
                

