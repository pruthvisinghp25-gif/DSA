class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        grater_element = []

        for i in nums1:
            
            idx = nums2.index(i)
            
            # found = False
            
            for j in range(idx + 1, len(nums2)):
            
                if i < nums2[j]:
                     grater_element.append(nums2[j])
                    #  found = True
                     break
            
            # if not found:
            else:
                grater_element.append(-1)
                   
        return grater_element
                
            

        
        