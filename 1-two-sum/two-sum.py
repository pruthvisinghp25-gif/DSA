class Solution(object):
    def twoSum(self, nums, target):
        freq = {}

        for i in range(len(nums)):
            find = target - nums[i]

            if find not in freq:
                freq[nums[i]] = i

            else:
                return [freq[find], i]




















        # freq = {}
        
        # for i in range(len(nums)):
        #     find = target - nums[i]
        
        #     if find in freq:
        #         return [freq[find], i]

        #     freq[nums[i]] = i                

