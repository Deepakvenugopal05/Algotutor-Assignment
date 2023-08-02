from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for row in matrix:
            for n in row:
                res.append(n)
        return res[k-1]