class Solution:
    def minimumDistance(self, word: str) -> int:
        # Helper function to calculate Manhattan distance on the 6-column keyboard
        def get_dist(p1: int, p2: int) -> int:
            # 26 represents an unplaced finger (cost to place is 0)
            if p1 == 26: 
                return 0
            return abs(p1 // 6 - p2 // 6) + abs(p1 % 6 - p2 % 6)
        
        memo = {}
        
        # dp(i, other) returns the min distance to type word[i:] 
        # given the other finger is at 'other'
        def dp(i: int, other: int) -> int:
            # Base case: reached the end of the word
            if i == len(word):
                return 0
            
            if (i, other) in memo:
                return memo[(i, other)]
            
            # Map current and previous characters to 0-25 integers
            curr = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A') if i > 0 else 26
            
            # Option 1: Use the finger currently on 'prev' to type 'curr'.
            # The 'other' finger stays where it is.
            cost1 = get_dist(prev, curr) + dp(i + 1, other)
            
            # Option 2: Use the finger currently on 'other' to type 'curr'.
            # The 'prev' finger now becomes the new 'other' finger.
            cost2 = get_dist(other, curr) + dp(i + 1, prev)
            
            memo[(i, other)] = min(cost1, cost2)
            return memo[(i, other)]
        
        # Start at index 0, with the "other" finger completely unplaced (26)
        return dp(0, 26)
        