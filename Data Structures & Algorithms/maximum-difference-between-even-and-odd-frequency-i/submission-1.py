class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = {}

        for c in s:
            if c in freqs:
                freqs[c] += 1
            else:
                freqs[c] = 1
        
        even_freqs = []
        odd_freqs = []
        for c, freq in freqs.items():
            if freq % 2 == 0: 
                even_freqs.append(freq)
            else:
                odd_freqs.append(freq)
        
        return max(odd_freqs) - min(even_freqs)
        