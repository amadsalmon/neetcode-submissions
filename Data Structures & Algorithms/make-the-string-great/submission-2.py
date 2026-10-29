class Solution:
    def makeGood(self, s: str) -> str:

        def containsAdjacent(s: str) -> bool:
            for i in range(1, len(s)):
                if (
                    s[i-1].lower() == s[i].lower() 
                    and (
                        (s[i-1].isupper() and s[i].islower())
                        or (s[i-1].islower() and s[i].isupper())
                    )
                    ):
                    return i-1
            return -1
        
        c = containsAdjacent(s) 
        if c != -1:
            s = s[:c] + s[c + 2:]
            return self.makeGood(s)
        
        return s
        
