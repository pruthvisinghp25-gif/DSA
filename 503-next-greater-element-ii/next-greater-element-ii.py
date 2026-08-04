class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        ngn = {}
        i = 0
        
        while len(ngn.keys()) != len(nums):
            cur = nums[i]
            if s and i == s[-1]:
                ngn[i] = -1
                s.pop()
            else:
                if s:
                    while s and cur > nums[s[-1]]:
                        ngn[s.pop()] = cur
                if i not in ngn and i not in s:
                    s.append(i)
            
            i = (i + 1)%len(nums)
        
        print(ngn)
        
        result = []
        for j in range(len(nums)):
            result.append(ngn[j])
        return result
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [-1] * n
#         stack = []

#         for i in range(2*n-1, -1, -1):
#             while stack and stack[-1] <= nums[i % n]:
#                 stack.pop()
                
#             if stack:
#                 ans[i % n] = stack[-1]

#             stack.append(nums[i % n])

#         return ans
