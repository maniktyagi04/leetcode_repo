class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s=s.strip()

        lst_wrd=s.split(" ")[-1]

        return len(lst_wrd)