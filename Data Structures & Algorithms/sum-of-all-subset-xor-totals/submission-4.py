class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(arr: List[int]) -> int:
            xor = 0
            for n in arr:
                xor ^= n
            return xor

        def backtrack(index: int, current_elements: List[int]) -> int:
            if index == len(nums):
                return xor(current_elements)
            
            current_elements.append(nums[index])
            include = backtrack(index + 1, current_elements)
            current_elements.pop()
            exclude = backtrack(index + 1, current_elements)

            return include + exclude

        return backtrack(0, [])
