class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        freq = {}
      
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                freq[nums2[i]] = -1
            else:
                freq[nums2[i]] = stack[-1]
                
            stack.append(nums2[i])

        ans = []

        for i in nums1:
            if i in freq:
                ans.append(freq[i])
        
        return ans

            

            

            
            



            
        
        
        
        
        
        
        
        
        
        
        
        
        
        # [brutal foarce approach]
        # grater_element = []

        # for i in nums1:
            
        #     idx = nums2.index(i)
            
        #     # found = False
            
        #     for j in range(idx + 1, len(nums2)):
            
        #         if i < nums2[j]:
        #              grater_element.append(nums2[j])
        #             #  found = True
        #              break
            
        #     # if not found:
        #     else:
        #         grater_element.append(-1)
                   
        # return grater_element
                
            

        
        