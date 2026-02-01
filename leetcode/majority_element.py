from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for k in freq:
            if freq[k] > len(nums) // 2:
                return k
        return nums[0]
