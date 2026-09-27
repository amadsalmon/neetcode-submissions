from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Best possible answer will have the length of t
        len_best_answer = len(t)
        
        # Build target frequency dict
        freqs = defaultdict(int)
        for letter in t:
            freqs[letter] += 1

        # Counters        
        needed = len(freqs)
        satisfied = 0
        l = 0
        min_len_found = 200000
        min_window_found = (-200000,200000)

        for r in range(len(s)):
            r_char = s[r]
            # 1. EXPAND 
            if r_char in freqs:
                freqs[r_char] -= 1
                if freqs[r_char] == 0:
                    satisfied += 1

            # 2. CONTRACT
            while satisfied == needed:
                current_len = r - l + 1
                if current_len < min_len_found:
                    min_len_found = current_len
                    min_window_found = (l,r)
                if current_len == len_best_answer: 
                    # Early return if we find a best possible answer (min possible length)
                    return s[l : r + 1]
                
                # Move L until the next wanted letter
                l_char = s[l]
                if l_char in freqs:
                    if freqs[l_char] == 0:
                        satisfied -= 1
                    freqs[l_char] += 1
                l += 1
                    
        # Now find the answer with the minimum length out of what we found
        return s[min_window_found[0] : min_window_found[1]+1] if min_window_found != (-200000,200000) else ""

