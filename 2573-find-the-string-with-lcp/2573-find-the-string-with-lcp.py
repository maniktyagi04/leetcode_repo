from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = [''] * n
        c = 97  # ord('a')
        
        # Step 1: Greedily construct the string
        for i in range(n):
            if not ans[i]:
                # If we need more than 26 characters, it's impossible
                if c > 122:  # ord('z')
                    return ""
                
                char_c = chr(c)
                for j in range(i, n):
                    # If lcp > 0, they must be the same character
                    if lcp[i][j] > 0 and not ans[j]:
                        ans[j] = char_c
                c += 1
                
        # Step 2: Validate the given LCP matrix against our constructed string
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if ans[i] == ans[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                    
                # Check if the current lcp matches the expected mathematical relation 
                # and check for matrix symmetry simultaneously
                if lcp[i][j] != expected or lcp[j][i] != expected:
                    return ""
                    
        return "".join(ans)