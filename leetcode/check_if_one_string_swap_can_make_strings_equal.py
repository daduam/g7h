from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        bad_count = 0
        for tp in zip(s1, s2):
            if tp[0] != tp[1]:
                bad_count += 1
        return bad_count <= 2 and Counter(s1) == Counter(s2)
