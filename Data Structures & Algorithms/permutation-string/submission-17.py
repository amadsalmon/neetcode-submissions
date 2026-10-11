from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqs = defaultdict(int)
        for letter in s1:
            freqs[letter] += 1

        def freqs_at_zero() -> bool:
            return not any([freq for freq in freqs.values()])

        l, r = 0, 0
        while r < len(s2):
            if s2[r] in freqs:
                freqs[s2[r]] -= 1

            if r - l + 1 == len(s1):
                if freqs_at_zero():
                    return True

                l_copy = s2[l]
                if l_copy in freqs:
                    freqs[l_copy] += 1
                l += 1
            
            r += 1
            
        return False
                    
        