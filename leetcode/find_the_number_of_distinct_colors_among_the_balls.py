from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball2color = dict()
        color2balls = defaultdict(set)
        ans = []
        for x, y in queries:
            if x in ball2color:
                prev = ball2color[x]
                color2balls[prev].remove(x)
                if len(color2balls[prev]) == 0:
                    color2balls.pop(prev)
            ball2color[x] = y
            color2balls[y].add(x)
            ans.append(len(color2balls))
        return ans
