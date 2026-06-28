class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        First, transform array to set.

        Iterate over each item of array.
        Determine if it is start of chain or not == is item-1 NOT in array? If False, skip item. 
        If True: keep incrementing and checking if the incremented value is in set until not. 
        Keep track of count. If currentCount > maxCount, replace maxCount

        Once iteration on array finished, return maxCount
        """

        s = set(nums)

        maxChainLength = 0

        for n in nums:
            # Determing if n is a sequence start 
            if n-1 not in s:
                currentChainLength = 1
                target = n + 1
                while target in s:
                    currentChainLength += 1
                    target += 1
                if currentChainLength > maxChainLength:
                    maxChainLength = currentChainLength

        return maxChainLength

