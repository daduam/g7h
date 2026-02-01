from collections import Counter
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num2freq = Counter(nums)
        for k in num2freq:
            if num2freq[k] > 1:
                return True
        return False
