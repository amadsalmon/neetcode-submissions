
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find max in pile: O(N)
        max_pile = max(piles)

        def timeToEatAllBananas(pace: int) -> int:
            from math import ceil
            return sum([ceil(num_of_bananas/pace)for num_of_bananas in piles])
        
        # k is bounded between 1 and max_pile (eating more bananas per hour than max_pile doesn't make sense)
        # So doing a binary search on values of k makes sense and helps us find optimal k in O(log(max_pile)*N)
        left = 1
        right = max_pile 
        min_k = max_pile

        while left <= right:
            k = (left + right) // 2
            if timeToEatAllBananas(k) <= h:
                right = k - 1
                min_k = k
            else:
                left = k + 1
        
        return min_k