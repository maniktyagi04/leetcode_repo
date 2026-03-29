class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if the characters at even indices (0, 2) can be matched
        even_match = (
            (s1[0] == s2[0] and s1[2] == s2[2]) or 
            (s1[0] == s2[2] and s1[2] == s2[0])
        )
        
        # Check if the characters at odd indices (1, 3) can be matched
        odd_match = (
            (s1[1] == s2[1] and s1[3] == s2[3]) or 
            (s1[1] == s2[3] and s1[3] == s2[1])
        )
        
        # Both even and odd positions must be resolvable for the strings to be equal
        return even_match and odd_match
        