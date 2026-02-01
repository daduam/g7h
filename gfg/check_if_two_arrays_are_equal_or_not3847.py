from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        freqa = Counter(a)
        freqb = Counter(b)
        return freqa == freqb
