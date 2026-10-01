from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1

        def findNumWithMaxFreq(freqs) -> int:
            numWithMaxFreq = None
            maxFreq = 0
            for n, freq in freqs.items():
                if freq > maxFreq:
                    maxFreq = freq
                    numWithMaxFreq = n
            return numWithMaxFreq

        result = []

        for i in range(k):
            n = findNumWithMaxFreq(freqs)
            freqs.pop(n)
            result.append(n)
        
        return result
        

        