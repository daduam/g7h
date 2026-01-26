class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            if i == len(strs[0]):
                break
            current_char = strs[0][i]
            for s in strs:
                if len(s) <= i or s[i] != current_char:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
