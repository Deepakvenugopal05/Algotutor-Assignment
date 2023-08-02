from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        ans = [sum(i) for i in accounts]

        return max(ans)
