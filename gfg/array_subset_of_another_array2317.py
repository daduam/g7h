from collections import Counter

class Solution:
    def isSubset(self, a, b):
        freqa = Counter(a)
        freqb = Counter(b)
        return freqb <= freqa
