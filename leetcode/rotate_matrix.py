from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Solution.transpose(matrix)
        Solution.reflect(matrix)

    @staticmethod
    def transpose(matrix):
        R, C = len(matrix), len(matrix[0])

        for r in range(R):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    @staticmethod
    def reflect(matrix):
        R, C = len(matrix), len(matrix[0])

        n = len(matrix[0]) - 1
        for r in range(R):
            left = 0
            right = n
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1