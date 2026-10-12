class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0: return []
        
        res = []

        def backtrack(index: int, elements: List[int]) -> None:
            if index == len(nums):
                return 
            elif sum(elements) == target:
                res.append(list(elements))
                return
            elif sum(elements) > target:
                return

            # Include
            elements.append(nums[index])
            backtrack(index, elements)

            # Exclude
            elements.pop()
            backtrack(index + 1, elements)
        
        backtrack(0, [])

        return res
