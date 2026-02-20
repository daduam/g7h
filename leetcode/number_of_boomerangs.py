from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(p1: List[int], p2: List[int]) -> int:
            return (p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2

        ans = 0
        for i in points:
            dist2freq = defaultdict(int)
            for j in points:
                dist2freq[dist(i, j)] += 1
            for freq in dist2freq.values():
                ans += freq * (freq - 1)
        return ans
 