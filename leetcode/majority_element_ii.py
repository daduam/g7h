from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        answer = []
        for num in freq:
            if freq[num] > len(nums) // 3:
                answer.append(num)
        return answer
