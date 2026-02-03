from typing import List
from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        snums = sorted(nums)
        idx = defaultdict(lambda: n)
        for i in range(n):
            idx[snums[i]] = min(idx[snums[i]], i)
        return [idx[x] for x in nums]
