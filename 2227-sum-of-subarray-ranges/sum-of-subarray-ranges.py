class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        range_max = 0

        for i, val in enumerate(nums + [float('inf')]):
            while stack and stack[-1][1] < val:
                k, j = stack.pop()
                
                left = k - stack[-1][0] if stack else k + 1
                right = i - k
                
                range_max += j * left * right 

            stack.append((i, val))

        stack = []
        range_min = 0 

        for i, val in enumerate(nums + [float('-inf')]):
            while stack and stack[-1][1] > val:
                k, j = stack.pop()

                left = k - stack[-1][0] if stack else k + 1
                right = i - k

                range_min += j * left * right

            stack.append((i, val))

        return range_max - range_min

    