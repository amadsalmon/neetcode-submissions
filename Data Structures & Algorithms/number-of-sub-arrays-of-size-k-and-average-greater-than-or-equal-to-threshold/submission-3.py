class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        running_sum = 0

        for r in range(len(arr)):
            running_sum += arr[r]
            
            if (r - l + 1) == k:
                if (running_sum / k) >= threshold:
                    res += 1
                running_sum -= arr[l]
                l += 1
                
        return res