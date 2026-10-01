from collections import defaultdict
from heapq import heapify, heappop

class Solution:

    """
    I will have to do a first pass on the nums array to transform it into a freqs dict, that I cannot avoid.
    Then I put each number in an array where the index represents the frequency of that number.
    Then I go from the end of the array and take k elements.

    Done.

    So operations would be: O(N + N + k) = O(N)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        arr_by_freq = [[] for _ in range(len(nums) + 1)]

        for n, freq in freqs.items():
            arr_by_freq[freq].append(n)
           
        k_largest = []
        i = len(arr_by_freq) - 1
        while i>=0 and len(k_largest) != k:
            if len(arr_by_freq[i]) > 0:
                n = arr_by_freq[i].pop()
                k_largest.append(n)
            else:
                i -= 1

        return k_largest
        

        