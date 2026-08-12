class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in matrix:

            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1

                else:
                    heights[j] = 0

            stack = []
            ext = heights + [0]

            for i, h in enumerate(ext):
                while stack and ext[stack[-1]] > h:
                    height = ext[stack.pop()]

                    left = stack[-1] if stack else -1
                    width = i - left - 1

                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area 