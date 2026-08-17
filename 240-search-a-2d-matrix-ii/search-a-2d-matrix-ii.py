class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                row += 1

            else:
                col -= 1

        return False

            