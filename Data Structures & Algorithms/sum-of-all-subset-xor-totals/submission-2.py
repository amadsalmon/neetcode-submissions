class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(a: int, b: int) -> int:
            return a ^ b

        res = 0


        def rec_xor(index, current_xor):
            if index == len(nums):
                return current_xor

            new_xor = xor(current_xor, nums[index])
            
            return rec_xor(index + 1, current_xor) + rec_xor(index + 1, new_xor)
            
        return rec_xor(0, 0)