class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        freq = {0:1}
        prfx_sum = 0
        count = 0

        for num in nums:
            prfx_sum += num

            need = prfx_sum - goal 

            if need in freq:
                count += freq[need]

            freq[prfx_sum] = freq.get(prfx_sum, 0)+1

        return count 


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        # res = 0
        # freq = {0:1}

        # for num in nums:
        #     count += num

        #     if count - goal in freq:
        #         res += freq[count - goal]

        #     freq[count] = freq.get(count, 0) + 1

        # return res

        
             
        