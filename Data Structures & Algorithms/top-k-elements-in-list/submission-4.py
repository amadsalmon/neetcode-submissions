from collections import defaultdict
from heapq import heapify, heappop

class Solution:

    """
    I will have to do a first pass on the nums array to transform it into a freqs dict, that I cannot avoid.
    Then I transform the freqs dict into an array of tuples: (freq, n).
    Then I transform that array into a min heap which will be sorted by freq, 
    which I then prune into keeping only K elements.

    Done.

    So operations would be: O(N + N + (N-k)*logN) = O(N*logN)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Build the frequencies - O(N)
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        # Transform frequencies into array of tuples - O(N)
        freqs = [(freq, n) for n, freq in freqs.items()]
            
        # Transform into heap O(N)
        heapify(freqs)

        # N-k times 
        while len(freqs) > k:
            # pop is O(logN)
            heappop(freqs)

        # Final pass: transform tuples into single nums only - O(k)
        k_largest = [num for freq, num in freqs]

        # So final time complexity is O(N + N + (N-k)*logN + k) = O(N*logN)
        return k_largest
        

        