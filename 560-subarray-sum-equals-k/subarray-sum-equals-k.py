class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        HashMap = {0 : 1}
        count = 0
        prfx_sum = 0

        for num in nums:
            prfx_sum += num
            count += HashMap.get(prfx_sum - k, 0)
            HashMap[prfx_sum] = HashMap.get(prfx_sum, 0) + 1

        return count 

        #     need = prfx_sum - k

        #     if need in HashMap:
        #         count += HashMap[need]
                
        #     HashMap[prfx_sum] = HashMap.get(prfx_sum, 0) + 1

        # return count 
