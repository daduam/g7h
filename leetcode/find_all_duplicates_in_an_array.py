from collections import Counter
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [x for x in freq if freq[x] == 2]
