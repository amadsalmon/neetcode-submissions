class Solution:

    """
    Better two-pass solutiom with O(N) complexity
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # First pass
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            
        # Second pass
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output
        

    """
    Naive solution, O(N^2) complexity
    """
    def productExceptSelf_v0(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        i = 0

        while i < len(nums):
            x = 0
            while x < len(nums):
                if x != i:
                    output[i] *= nums[x]
                x += 1 
            i += 1

        return output