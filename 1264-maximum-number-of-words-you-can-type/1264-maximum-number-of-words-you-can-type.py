class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)   # store broken letters in a set
        words = text.split()          # split the text into words
        count = 0
        
        for word in words:
            if not (set(word) & broken):  # if word has no broken letter
                count += 1
        
        return count

        