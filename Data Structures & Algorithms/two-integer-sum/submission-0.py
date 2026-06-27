class Solution:
    """
    Obvious first solution: iterate through each pair of the array until we find a pair that 
    sums up to target. 
    That's O(N^2). Let's try to find something smarter, in O(N).
    I am thinking of two ways of doing that. 
    
    B) Dictionary
    The equation is nums[i] + nums[j] == target (given i != j). That means for each nums[i], 
    we know we need nums[j] to be equal to (target -  nums[i]) for (i,j) to be a suitable pair.
    By going first through the array and storing the elements in a dictionary, we can then know 
    for each nums[i] if we have a suitable nums[j] = (target -  nums[i]). 
    That's O(N).

    C) If we start by sorting the array, then we can probably have a fast & slow pointer iteration.
    
    """

    def findInSeenIndices(self, seen_indices: List[int], index_to_skip: int):
        for index in seen_indices:
            if index != index_to_skip:
                return index
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Init dictionary
        seen = {}
        for index in range(0, len(nums)):
            num = nums[index]
            if num not in seen: 
                seen[num] = [index]
            else:
                seen[num] += [index]

        
        for i in range(0, len(nums)):
            difference = target -  nums[i]
            if difference in seen:
                j = self.findInSeenIndices(seen[difference], i)
                if j != -1:
                    return [i, j] 
        
        return [-1,-1]
            


        