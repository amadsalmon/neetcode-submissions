class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freq = 1
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
                freq = freqs[num]
        
        freqs_arr = [[] for _ in range(0, len(nums)+1)]
        for num, freq in freqs.items():
            freqs_arr[freq].append(num)


        i = len(freqs_arr) - 1
        res = []
        while i >= 0 and len(res)<k:
            if freqs_arr[i] and freqs_arr[i]!=0 :
                res += freqs_arr[i]
            i -= 1  
        
        return res
    
            