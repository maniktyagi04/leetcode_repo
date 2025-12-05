class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prfx = strs[0]
        for l in strs[1:]:
            while not l.startswith(prfx):
                prfx = prfx[:-1]
                if not prfx:
                    return ""
        return prfx