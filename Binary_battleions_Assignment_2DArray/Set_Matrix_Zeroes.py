from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vals = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    vals.append((i,j))
        for axis in vals:
            for i in range(len(matrix)):
                matrix[i][axis[1]] = 0
            for j in range(len(matrix[0])):
                matrix[axis[0]][j] = 0
