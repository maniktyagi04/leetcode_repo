class Solution:
    def countTriples(self, n: int) -> int:
        import math
        cnt = 0
        for c in range(1, n+1):
            c2 = c * c
            for a in range(1, c):
                b2 = c2 - a*a
                if b2 <= 0:
                    continue
                b = math.isqrt(b2)
                if b * b == b2: 
                    cnt += 1     
        return cnt
