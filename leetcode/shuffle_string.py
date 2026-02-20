from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = ['0'] * len(s)
        for i in range(len(s)):
            temp[indices[i]] = s[i]
        return ''.join(temp)
