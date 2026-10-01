from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        # O(N)
        for n in nums:
            freqs[n] += 1
        
        # O(N)
        def findNumWithMaxFreq(freqs) -> int:
            numWithMaxFreq = None
            maxFreq = 0
            for n, freq in freqs.items():
                if freq > maxFreq:
                    maxFreq = freq
                    numWithMaxFreq = n
            return numWithMaxFreq

        result = []

        # O(k*N)
        for i in range(k):
            n = findNumWithMaxFreq(freqs)
            freqs.pop(n)
            result.append(n)

        # So final time complexity is O(N + k*N) = O(N) or actually O(N^2) if K~N
        
        return result
        

        