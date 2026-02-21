from typing import List

class Solution:
    dt = [(0,0),(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img) 
        m = len(img[0]) if n > 0 else 0
        ans = [[0] * m for _ in range(n)]

        for r in range(len(img)):
            for c in range(len(img[0])):
                count = 0
                total = 0
                for di, dj in self.dt:
                    nr, nc = r + di, c + dj
                    if 0 <= nr < n and 0 <= nc < m:
                        count += 1
                        total += img[nr][nc]
                ans[r][c] = total // count
        
        return ans
