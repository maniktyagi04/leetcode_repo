from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        if n == 0:
            return 1


        vals = sorted(set(complexity))
        comp_index = {v: i+1 for i, v in enumerate(vals)}  
        m = len(vals)


        INF = 10**9
        bit = [INF] * (m+1)
        def bit_update(pos, val):
            while pos <= m:
                if val < bit[pos]:
                    bit[pos] = val
                pos += pos & -pos
        def bit_query(pos):  
            res = INF
            while pos > 0:
                if bit[pos] < res:
                    res = bit[pos]
                pos -= pos & -pos
            return res


        parent = [-1] * n

        bit_update(comp_index[complexity[0]], 0)

        for i in range(1, n):
            ci = comp_index[complexity[i]]

            if ci - 1 >= 1:
                p = bit_query(ci - 1)
            else:
                p = INF
            if p == INF:
                return 0  
            parent[i] = p

            bit_update(ci, min(bit_query(ci) , i))  


        children = [[] for _ in range(n)]
        root = 0
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)


        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (n+1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD


        import sys
        sys.setrecursionlimit(1 << 25)
        def dfs(v):
            total_size = 0   
            ways = 1

            child_sizes = []
            for c in children[v]:
                sz_c, ways_c = dfs(c)
                total_size += sz_c
                ways = ways * ways_c % MOD
                child_sizes.append(sz_c)

            ways = ways * fact[total_size] % MOD
            for sz in child_sizes:
                ways = ways * invfact[sz] % MOD

            return total_size + 1, ways

        _, answer = dfs(root)
        return answer % MOD
