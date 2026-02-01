from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = dict()
        for match in matches:
            if match[0] not in losers:
                losers[match[0]] = 0
            if match[1] not in losers:
                losers[match[1]] = 0
            losers[match[1]] += 1
        answer = [[], []]
        for k in losers:
            if losers[k] == 0:
                answer[0].append(k)
            if losers[k] == 1:
                answer[1].append(k)
        answer[0].sort()
        answer[1].sort()
        return answer
