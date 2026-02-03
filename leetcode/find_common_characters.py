from collections import defaultdict, Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = defaultdict(lambda: 101)
        for word in words:
            counter = Counter(word)
            for i in range(26):
                k = chr(ord('a') + i)
                freq[k] = min(freq[k], counter.get(k, 0))
        result = []
        print(freq)
        for k in freq:
            if freq[k] == 101:
                continue
            for i in range(freq[k]):
                result.append(k)
        return result
