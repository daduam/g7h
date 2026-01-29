from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_covered = True
        for i in range(left, right+1):
            temp_covered = False
            for rr in ranges:
                temp_covered = temp_covered or (i >= rr[0] and i <= rr[1])
            all_covered = all_covered and temp_covered
        return all_covered
