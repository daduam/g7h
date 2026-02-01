from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = [(num, i) for i, num in enumerate(nums)]
        num_to_idx.sort()
        left, right = 0, len(num_to_idx) - 1
        while left < right:
            cursum = num_to_idx[left][0] + num_to_idx[right][0]
            if cursum > target:
                right -= 1
            elif cursum < target:
                left += 1
            else:
                break
        return [num_to_idx[left][1], num_to_idx[right][1]]
