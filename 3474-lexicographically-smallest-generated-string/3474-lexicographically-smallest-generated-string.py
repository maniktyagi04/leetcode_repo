class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        
        # ans array holds the characters, '?' denotes an unassigned state initially
        ans = ['?'] * L
        fixed = [False] * L
        
        # 1. Apply all 'T' (forced) constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if not fixed[i+j]:
                        ans[i+j] = str2[j]
                        fixed[i+j] = True
                    elif ans[i+j] != str2[j]:
                        # Contradiction found between two overlapping 'T' requirements
                        return ""
                        
        # 2. Fill all remaining flexible positions with 'a' for lexicographically smallest base
        for i in range(L):
            if not fixed[i]:
                ans[i] = 'a'
                
        # 3. Resolve all 'F' constraints sweeping left to right
        list_str2 = list(str2)
        for i in range(n):
            if str1[i] == 'F':
                # If an 'F' constraint accidentally matches str2 perfectly, we must break the match
                if ans[i:i+m] == list_str2:
                    flipped = False
                    
                    # Flip the rightmost unfixed 'a' to a 'b'
                    for j in range(m - 1, -1, -1):
                        if not fixed[i+j]:
                            ans[i+j] = 'b'
                            fixed[i+j] = True
                            flipped = True
                            break
                            
                    # If the entire matching window was locked by 'T' constraints, we cannot resolve the issue
                    if not flipped:
                        return ""
                        
        return "".join(ans)