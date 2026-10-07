from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l, r = 0, 0
        maxes = []

        while r < len(nums):
            while q and q[-1][1] <= nums[r]:
                q.pop()
            q.append([r, nums[r]])

            if r - l + 1 == k:  # is our sliding window of size k?
                maxes.append(q[0][1])
                l += 1
                while q and q[0][0] < l:
                    q.popleft()                

            r += 1
        
        return maxes


"""
   0, 3, 1, 2, 0
         l
               r

len(nums) = 5
k = 3
q = [ (3, 2), (4, 0)]
l = 2
r = 4
maxes = [3, 3, 2 ]

"""        