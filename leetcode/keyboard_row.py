from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        answer = []
        for word in words:
            chars = set(word.lower())
            if chars.issubset(first_row) or chars.issubset(second_row) or chars.issubset(third_row):
                answer.append(word)
        return answer
        