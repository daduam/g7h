from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        wordToIdx = dict()
        minIdxSum = float('inf')
        for i, word in enumerate(list1):
            if word in wordToIdx:
                continue
            wordToIdx[word] = [i, -1]
        for i, word in enumerate(list2):
            if word not in wordToIdx:
                continue
            if wordToIdx[word][1] > -1:
                continue
            wordToIdx[word][1] = i
            minIdxSum = min(minIdxSum, sum(wordToIdx[word]))
        answer = []
        for k, v in wordToIdx.items():
            if v[1] == -1:
                continue
            if sum(v) == minIdxSum:
                answer.append(k)
        return answer
 