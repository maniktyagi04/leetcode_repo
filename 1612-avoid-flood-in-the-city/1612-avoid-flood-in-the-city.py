
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        last = {}
        zeros = []
        for i, lake in enumerate(rains):
            if lake == 0:
                zeros.append(i)
            else:
                if lake in last:
                    prev = last[lake]
                    idx = bisect_right(zeros, prev)
                    if idx == len(zeros):
                        return []
                    dry = zeros.pop(idx)
                    ans[dry] = lake
                last[lake] = i
                ans[i] = -1
        return ans






